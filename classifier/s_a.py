#!/usr/bin/python

__Vrasinavaru__='Eshak'

import sys
import mysql.connector
from nltk.sentiment.vader import SentimentIntensityAnalyzer

fo = open("sentiment_analysis.txt", "w")
outStr = ""
currIndex = 0

try:
    conn = mysql.connector.connect(user='r_acc', password='test', host='127.0.0.1', database='r_db')

    cursor = conn.cursor()

    query = ("select title, subreddit, year from all_threads")

    cursor.execute(query)

    sia = SentimentIntensityAnalyzer()
    for post_title, subreddit, year in cursor:
        currIndex += 1
        modified_title = post_title.encode('utf-8')
        print str(currIndex) + ": " + modified_title + "\n"
        outStr = str(year) + "\t" + modified_title + "\t" + subreddit.encode('utf-8')
        scores = sia.polarity_scores(modified_title)
        for k in sorted(scores):
            # compound, negative, neutral, positive
            outStr += "\t" + str(scores[k])
            #print ('{0}: {1}, '.format(k, ss[k])),
        fo.write(outStr + "\n")
        outStr = ""

    cursor.close()
    conn.close()
except:
    error_value = sys.exc_info()[1]
    print ('Failed: ',  error_value)
