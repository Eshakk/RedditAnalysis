__author__ = 'Potula1'

'''
Loaded data into database r_db;
Using output files containing information regarding each reddit post into table all_threads, partitioned by year
load data local infile '/Users/Potula1/Downloads/RedditAnalysis-master/output/output_1450028456.txt' ignore into table all_threads fields terminated by '\t' lines terminated by '\n' (year, title, num_of_comments, num_of_upvotes, source, subreddit);
'''

import mysql.connector
from nltk.corpus import stopwords
import heapq
import nltk

cnx = mysql.connector.connect(user="r_acc",password="test",host="127.0.0.1",database="r_db")
cursor = cnx.cursor()
query = 'select distinct(subreddit) from all_threads'
cursor.execute(query);

subreddit_topics = []
for i,j in cursor:
    print i,j
    subreddit_topics.append(i)

def remove_stop_words(title):
    line = ''
    t = title.split()
    for word in t:
        if(word.lower() not in stopwords.words('english')):
            line += word
            line += ' '
    return line

thread = []
all_words = []

def remove_adjectives(words):
    line = ''
    tagged = nltk.pos_tag(words)
    for i in tagged:
        if(i[1] not in ['DT','JJ','RB']):
            print ("Stupid dheeraj")

cnx = mysql.connector.connect(user="r_acc",password="test",host="127.0.0.1",database="r_db")
cursor = cnx.cursor()
for i in subreddit_topics:
    query = 'select title from all_threads where subreddit = "' + str(i) + '";'
    print query
    cursor.execute(query)
    for title in cursor:
        line = remove_stop_words(title[0])
        #line = remove_adjectives(line.split())
        all_words += line.split()
    thread.append([i,all_words])
    all_words = []

heap = []
thread_dict = []
reddit_dict = {}
for words_set in thread:
    for word in words_set[1]:
        if(reddit_dict.get(word,-1) == -1):
            reddit_dict[word] = 1
        else:
            reddit_dict[word] += 1
    thread_dict.append([words_set[0],reddit_dict])
    reddit_dict = {}

heap = []
for line in thread_dict:
    print '--------------'
    print line[0]
    print
    for key in line[1]:
        heapq.heappush(heap,(line[1][key],key))
    print heapq.nlargest(15,heap)
    heap = []
