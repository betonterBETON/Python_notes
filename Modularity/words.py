import sys  # lets us accept command line arguments
from urllib.request import urlopen


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):  # this will print ANY iterable collection
    # such as a string, one char per line...
    # or such as a list of numbers
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)  # 'http://sixty-north.com/c/t.txt'
    print_items(words)  # now we can test in REPL, by (import *, main('htttp...txt')


if __name__ == '__main__':
    main(sys.argv[1])  # ... and also it will work when executed with arg in cmd line
