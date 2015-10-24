import sys
import json

def main():
    occurrences = {}

    tweet_file = open(sys.argv[1])

    for line in tweet_file:
        line = line.encode('utf-8')
        a = json.loads(line)

        if "entities" in a.keys():
            entities = a["entities"]
            if "hashtags" in entities.keys():
                hashtags = a["entities"]["hashtags"]
                if len(hashtags) > 0 :
                    for item in hashtags:
                        if "text" in item.keys():
                            hashtag = item["text"].encode('utf-8')
                            if hashtag in occurrences.keys():
                                occurrences[hashtag] += 1
                            else:
                                occurrences[hashtag] = 1
        '''
        if "user" in a.keys():
            user = a["user"]
            print user.keys()
            if "entities" in user.keys():
                entities = user["entities"]
                print entities

                if "hashtags" in entities.keys():
                    hashtags = a["entities"]["hashtags"]
                    if len(hashtags) > 0 :
                        for item in hashtags:
                            if "text" in item.keys():
                                hashtag = item["text"].encode('utf-8')
                                if hashtag in occurrences.keys():
                                    occurrences[hashtag] += 1
                                else:
                                    occurrences[hashtag] = 1
                '''
    place = 1
    for key in sorted(occurrences, key=occurrences.get, reverse=True):
        if place > 10:
            break
        print ("%s %f") % (key, occurrences[key])
        place += 1

if __name__ == '__main__':
    main()
