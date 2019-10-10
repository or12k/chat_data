
def read_fchat():
    """open a chat text file and read through it"""
    chat_file = input("Enter text file:")
    chat_path = open(chat_file, encoding="utf-8")
    chat_text = chat_path.read()
    chat_path.close()

    return chat_text


def main():
    """ read chat text and turn them into sorted information"""
    chat = read_fchat()
    # print all text
    print(chat)


if __name__ == "__main__":
    main()
