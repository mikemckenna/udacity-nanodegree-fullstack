import urllib


def read_file():
    file1 = open("profanity_screener/movie_quotes.txt")
    file_content = file1.read()
    print(file_content)
    file1.close()
    check_profanity(file_content)


def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profanity detected in searched text!")
    elif "false" in output:
        print("No profanity detected in searched text")
    else:
        print("Could not screen text for profanity")

read_file()
