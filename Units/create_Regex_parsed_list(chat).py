import re


def read_fchat():
    """open a chat text file and read through it"""
    chat_file = input("Enter chat text file:")
    chat_path = open(chat_file, encoding="utf-8")
    chat_text = chat_path.read()
    chat_path.close()

    return chat_text


def create_Regex_parsed_list(chat):
    """create a messages list, parsed by time, date, author, content .

    pass-the chat to retrive messages
    use regex to parse the text"""
    regex_chat = r'(\d{2}\/\d{2}\/\d{4}),\s(\d(?:\d)?:\d{2})\s-\s([^:]*):\s(.*?)(?=\s*\d{2}\/|\$)'
    regex_Chat = re.compile(regex_chat, flags=re.M)
    # LIST of dates
    Chat_l = regex_Chat.findall(chat)
    return Chat_l


def main():
    """ read chat text and turn them into sorted information"""
    chat = read_fchat()
    msg = create_Regex_parsed_list(chat)
    print(msg)
    # creat_table(msg)


if __name__ == "__main__":
    main()
