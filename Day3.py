#This will have all the code practices that are done in day 2
#----------------------Collection Types----------------------
from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words=line.decode('utf-8').split()
    for word in line_words:
        story_words.append(word)
story.close()

for words in story_words:
    print(words)