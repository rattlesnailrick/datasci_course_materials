import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    '''
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    '''

    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary

    occurrences = {}
    term_score = {}
    term_score_mean = {}

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet_score = 0
        a = json.loads(line)
        if "lang" in a.keys():
            if a["lang"] == "en":
                if "text" in a.keys():
                    tweet = a["text"].encode('utf-8')
                    for word in tweet.split(" "):
                        if word in scores.keys():
                            tweet_score += scores[word]
                            #print word, scores[word]
                    for word in tweet.split(" "):
                        #print word
                        if word in occurrences:
                            occurrences[word] += 1
                        else:
                            occurrences[word] = 1
                        if word in term_score:
                            term_score[word] += tweet_score
                        else:
                            term_score[word] = tweet_score
    for key in term_score.keys():
        term_score_mean[key] = term_score[key]*1.0 / occurrences[key]

    for key in term_score_mean.keys():
        print key, term_score_mean[key]
    #print term_score_mean

if __name__ == '__main__':
    main()
