from urllib.request import urlopen


def fetch_words():  # now to run this code, first import words, then run words.fetch_words()
                    # or from words import fetch_words
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    for word in story_words:
        print(word)

# ^ this is not executable, that means, if called by python words.py in cmd, it will not yield
# any results!

print(__name__)  # this will produce "__main__" when executed as "python words.py"from shell
# and will produce "words" if imported (only for the first import, if it's done again,
# nothing will be printed. CODE EXECUTED ONLY ONCE AT 1ST IMPORT

if __name__ == '__main__':  # this will only run when executed as script (called from shell)
    # it will NOT run when imported
    fetch_words()