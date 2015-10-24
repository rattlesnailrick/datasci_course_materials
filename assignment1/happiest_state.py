import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    occurrences = {}
    sum_score = {}
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        score = 0


        a = json.loads(line)
        try:
            location = a["user"]["location"]
            location = location.encode('utf-8')
            for word in location.split(" "):
                if word in states.keys():
                    #state = states[word]
                    state = word
                    #print state
        except:
            state = "none"
        if "text" in a.keys():
            tweet = a["text"].encode('utf-8')
            for word in tweet.split(" "):
                if word in scores.keys():
                    score += scores[word]
                    if not state == "none":
                        if state in occurrences.keys():
                            occurrences[state] += 1
                            sum_score[state] += score
                        else:
                            occurrences[state] = 1
                            sum_score[state] = score
    mean_score = {}

    highscore = 0
    happiest_state = ""

    for key in occurrences.keys():
        mean_score[key] = sum_score[key]*1.0 /  occurrences[key]
        #print ("%s %2.4f") % (key, mean_score[key])
        if mean_score[key] > highscore:
            highscore = mean_score[key]
            happiest_state = key
    print happiest_state
if __name__ == '__main__':
    main()
