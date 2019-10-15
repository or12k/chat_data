
import sqlite3
import re


def read_fchat():
    """open a chat text file and read through it"""
    chat_file = input("Enter text file:")
    chat_path = open(chat_file, encoding="utf-8")
    chat_text = chat_path.read()
    chat_path.close()

    return chat_text


def create_parse_list(chat):
    """create a messages list, parsed by time, date, author, content .

    pass-the chat to retrive messages
    use regex to parse the text"""
    regex_chat = r'(\d{2}\/\d{2}\/\d{4}),\s(\d(?:\d)?:\d{2})\s-\s([^:]*):\s(.*?)(?=\s*\d{2}\/|\$)'
    regex_Chat = re.compile(regex_chat, flags=re.M)
    # LIST of dates
    Chat_l = regex_Chat.findall(chat)
    return Chat_l


def creat_table(list):  # need adjustments
    """create a table,to sort messages"""

    conn = sqlite3.connect('p.sqlite')
    cur = conn.cursor()

    cur.executescript('DROP TABLE IF EXISTS Messages')

    cur.execute('''
     CREATE TABLE Messages (id INTEGER,
     date  INTEGER,
     time INTEGER,
     author TEXT,
     content TEXT)''')

    for msg in list:
        date = msg[0]
        time = msg[1]
        author = msg[2]
        content = msg[3]
        #print(date, time, author, content)

        cur.execute('SELECT id FROM Messages WHERE date = ? ', (date,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Messages (date, time, author, content, id)
                    VALUES (?,?,?,?,1)''', (date, time, author, content, ))
        else:
            cur.execute('UPDATE Messages SET id = id + 1 WHERE date = ? ', (date,))
        conn.commit()

    sqlstr = 'SELECT id, date, time, author, content FROM Messages ORDER BY id DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0], row[1], row[2], row[3], row[4]))

    cur.close()


def main():
    """ read chat text and turn them into sorted information"""
    chat = read_fchat()
    messages = create_parse_list(chat)
    # print(msg)
    creat_table(messages)


if __name__ == "__main__":
    main()
