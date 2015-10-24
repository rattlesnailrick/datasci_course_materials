import sys
import json

def main():

    occurrences = {}
    total_words = 0

    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        a = json.loads(line)
        if "text" in a.keys():
            tweet = a["text"]
            tweet = tweet.encode('utf-8')
            words = tweet.split(" ")
            for word in words:
                word = ''.join(e for e in word if e.isalnum())
                if not word == "":
                    total_words += 1
                    if word in occurrences:
                        occurrences[word] += 1
                    else:
                        occurrences[word] = 1

    for word in occurrences.keys():
        print ("%s %f") % (word, occurrences[word]*1. / total_words)

if __name__ == '__main__':
    main()
