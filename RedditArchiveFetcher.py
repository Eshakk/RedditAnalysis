'''
Created on Dec 12, 2015

@author: Prashanth
'''
import re
from bs4 import BeautifulSoup
import requests
from idlelib.IOBinding import encoding
from time import sleep
import datetime
import os
import calendar
import time
import logging
import datetime
from datetime import date,timedelta as td
#December+10,+2015
date_list = []
today = datetime.date.today()
topList=[]
d1 = date(2015,12,10)
d2 = date(2015,12,12)
delta = d2 - d1

for i in range(delta.days + 1):
    fetch_date=(d1 + td(days=i)).strftime('%B+%d,+%Y')
    date_list.append(fetch_date)
    
#print(len(date_list))






logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='R:\CreativeChaos\Twentyment\TRACE_LOG.log',
                    filemode='w')

prevFileStamp="R:\CreativeChaos\Twentyment\output_"+ str(calendar.timegm(time.gmtime()))+".txt";
with open(prevFileStamp,"w") as x:
    x.write("\n");
    x.close()

for dateItem in date_list:    
    sleep(5)
    #Read from the URL and log
    url='http://www.redditarchive.com/?d='+dateItem
    r=requests.get(url)
    web_data=r.content
    soup=BeautifulSoup(web_data,"html.parser")
            



#with open('sample.txt', mode='r',encoding="utf_8") as myfile:
#    data=myfile.read()

    try:
            soup=BeautifulSoup(web_data,"html.parser")
            posts=soup.findAll('li',attrs={'class':"ri"})
            
            for post in posts:
                each_div=post.findAll("div")[0]
                
                
                try: 
                    
                    title=each_div.findAll("a",attrs={'class':'i_title'})
                    title_text=title[0].text
                    
                    cite=each_div.findAll('cite')
                    subreddit=str(cite[0].find("a"))
                    
                                       
                    i=subreddit.find("/r")
                    index=subreddit.find("/",i+3)
                    subreddit_text=subreddit[i:index]
                    
                    cite_text=cite[0].text.replace("Reddit -","")
                    
                    comments=each_div.findAll("span",attrs={'class':'aS'})[0].findAll("a")
                    comments_text=comments[0].text.replace(" Comments","")
                    
                    unvoted=each_div.findAll("div",attrs={'class':'score unvoted'})
                    unvoted_text=unvoted[0].text
                    
                    
                    data=str(title_text+ "\t"+ comments_text+"\t"+unvoted_text+"\t"+cite_text+"\t"+subreddit_text)
                    print(data)
                    topList.append(data)
                except:
                    print("Failed")               
                
                
                
                
                #print(title_text)
                
    except Exception as e:
        print("Failed")
        
     
    r.close()
    #If file size is greater than 50Mb open a new file
    if os.stat(prevFileStamp).st_size>6553600:
            print("Opening new file \n")
            prevFileStamp="R:\CreativeChaos\Twentyment\output_"+str(calendar.timegm(time.gmtime()))+".txt";
            
    with open(prevFileStamp, "a") as myfile:
        for item in topList:
            try:
                myfile.write("%s\n" % item)
            except:
                print("ERROR: Could not write this line");
           
    topList.clear()    
   
            
    
                
