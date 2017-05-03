# read into file
import re


def tweetsIn(filename):
    # reads in a file and turns words into lower case and removes
    # extraneous symbols (/.:;)
    file = open(filename, 'r')
    text = file.read().lower()
    file.close()

    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    # write function that reads tweets into words
    # print(words)
    return words

def wordCount(wordList):
    positive = tweetsIn('positivewords.txt')
    countPos = 0
    negative = tweetsIn('negativewords.txt')
    countNeg = 0

    # uncomment print(word) to see what words are being counted
    for word in wordList:
        for posWord in positive:
            if word == posWord:
                countPos = countPos +1
                # print(word)
        for negWord in negative:
            if word == negWord:
                countNeg = countNeg +1
                # print(word)

    return countNeg, countPos

if __name__ == '__main__':
    filename = 'tweets.txt'
    count = wordCount(tweetsIn(filename))
    print('Negative Words:', count[0])
    print('Positive Words:', count[1])
