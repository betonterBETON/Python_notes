from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()  # close url handle

print(story_words)  # we received a list of bytes object,
# that is because the HTTP request transfers raw bytes to us
# we can use bytes.decode() above there to get strings
