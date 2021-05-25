from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):  # this will print ANY iterable collection
    # such as a string, one char per line...
    # or such as a list of numbers
    # so "print words" isn't a great name, it's misleading
    for word in story_words:
        print(word)


def main():     # by putting main() in a separate function,
    # we can test the main block in the REPL (otherwise, we cound't call it from there,
    # if this block only appeared after the if-name-main idiom!)
    # then, in the REPL, do: "from words import main", and you can run it.
    words = fetch_words()
    print_words(words)


if __name__ == '__main__':
    main()