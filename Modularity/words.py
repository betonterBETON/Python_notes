# !usr/bin/env python3
# the shebang is also useful on windows
# py.exe (Pylauncher) located on the PATH parses the shebang
# and locates the right version of python


import sys  # lets us accept command line arguments
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

      Args:
          url: the URL of a UTF-8 text document.

      Returns:
          A list of strings containing the words from
          the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: an iterable series of printable items.

    Returns:
        None
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL.

    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        None
    """
    words = fetch_words(url)  # 'http://sixty-north.com/c/t.txt'
    print_items(words)  # now we can test in REPL, by (import *, main('htttp...txt')


if __name__ == '__main__':
    main(sys.argv[1])  # ... and also it will work when executed with arg in cmd line
    # sys.argv[0] is the module name
