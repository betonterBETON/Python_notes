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


def main():  # by putting main() in a separate function,
    # we can test the main block in the REPL (otherwise, we cound't call it from there,
    # if this block only appeared after the if-name-main idiom!)
    # then, in the REPL, do: "from words import main", and you can run it.
    url = sys.argv[1]  # argv is a list of strings, which make the cmd arguments!
    # this makes it unable to test from the REPL
    # via (import * main()) or even (import * main() http....txt) !!!
    words = fetch_words(url)  # 'http://sixty-north.com/c/t.txt'
    print_items(words)  # to get appropriate result, run: python3 words.py http://sixty-north.com/c/t.txt


if __name__ == '__main__':
    main()
