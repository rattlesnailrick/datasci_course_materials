import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        score = 0
        a = json.loads(line)
        if "lang" in a.keys():
            if a["lang"] == "en":
                if "text" in a.keys():
                    tweet = a["text"].encode('utf-8')
                    for word in tweet.split(" "):
                        if word in scores.keys():
                            score += scores[word]
                            #print word, scores[word]
        print score



if __name__ == '__main__':
    main()
