import time
import sqlite3
import re


def read_fchat():
    """open a chat text file and read through it"""
#chat_file = input("Enter text file:")
    chat_path = open('Wtap_pichman.txt', encoding="utf-8")
    chat_text = chat_path.read()
    chat_path.close()

    return chat_text


def create_TimeStamp_list(chat):
    """create a DateTimeStamp-messages list and save it in txt file.

    retrive DateTimeStamp- messages useing regex to parse the text
    Open and Close  file "DateTimeStamp.txt"""

    # LIST of time #[,]\s(\d(?:\d)?:\d{2})
    regex_time = r'[,]\s(\d(?:\d)?:\d{2})'
    regex_Time = re.compile(regex_time, flags=re.M)
    Time_l = regex_Time.findall(chat)
    return Time_l


def create_DateStamp_list(chat):
    # ,\s(\d(?:\d)?:\d{2})'#\s-\s([^:]*):\s(.*?)(?=\s*\d{2}\/|\$)'
    regex_date = r'(\d{2}\/\d{2}\/\d{4})'
    regex_Date = re.compile(regex_date, flags=re.M)
    Date_l = regex_Date.findall(chat)
    return Date_l


def creat_date_table(list):  # need adjustments
    """create a table,to sort messages"""

    conn = sqlite3.connect('DateStamp.sqlite')
    cur = conn.cursor()

    cur.executescript('DROP TABLE IF EXISTS DateStamp')

    cur.execute('''
     CREATE TABLE DateStamp (id INTEGER,
     date INTEGER)''')

    for i in list:
        date = i

        cur.execute('SELECT id FROM DateStamp WHERE date = ? ', (date,))
        row = cur.fetchone()
        # if row is None:
        cur.execute('''INSERT INTO DateStamp (date, id)
                VALUES (?,1)''', (date, ))
    #    else:
        cur.execute('UPDATE DateStamp SET id = id + 1 WHERE date = ? ', (date,))
        conn.commit()

    sqlstr = 'SELECT id, date FROM DateStamp ORDER BY date DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()


def creat_time_table(list):  # need adjustments
    """create a table,to sort messages"""

    conn = sqlite3.connect('TimeStamp.sqlite')
    cur = conn.cursor()

    cur.executescript('DROP TABLE IF EXISTS TimeStamp')

    cur.execute('''
     CREATE TABLE TimeStamp (id INTEGER,
     time INTEGER)''')

    for x in list:
        time = x

        #print(date, time, author, content)

        cur.execute('SELECT id FROM TimeStamp WHERE time = ? ', (time,))
        row = cur.fetchone()
        # if row is None:
        cur.execute('''INSERT INTO TimeStamp (time, id)
                VALUES (?,1)''', (time, ))
        # else:
        cur.execute('UPDATE TimeStamp SET id = id + 1 WHERE time = ? ', (time,))
        conn.commit()

    sqlstr = 'SELECT id, time FROM TimeStamp ORDER BY time DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])

    cur.close()


def main():
    start = time.clock()
    """ read chat text and turn them into sorted information"""
    chat = read_fchat()
    d = create_DateStamp_list(chat)
    t = create_TimeStamp_list(chat)
    creat_time_table(t)
    creat_date_table(d)
    end = time.clock()
    print("DateTimeStamp, measured time:", end-start)


if __name__ == "__main__":
    main()
