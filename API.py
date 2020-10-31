#getting all the API tweets:

import twitter
import pandas as pd
import csv
import time
import numpy as np


def API():
    twitter_api = twitter.Api(consumer_key='SyYb53RgRe2yovpNkbRLQWMLf',
                        consumer_secret='YxOG1Vs8mdUtgNI5dJqXSAIbKYm4fl0D8BgWcAQt8z6fLqxZKx',
                        access_token_key='1318702260596006912-nSG7CBJZHBAnwDQABFc4J8HOaNBwKL',
                        access_token_secret='mkabBMLcYMdRNFSPEvav5OEWFjBWImsCBTGsRnewEOr8q')
    print(twitter_api.VerifyCredentials())

    #first 100 tweets
    try:
        trump_tweets_1= twitter_api.GetSearch('trump', count = 40, lang='en')
        id_1=(len(trump_tweets_1))
        id_1=trump_tweets_1[id_1-1].id

    except:
        print("there is an error")




    trump_tweets=trump_tweets_1

    
    trump_text_tweets=[]
    trump_tweet_id=[]
    trump_tweet_screenname=[]
    trump_tweet_time=[]
    trump_tweet_subject=[]

    for x in range(0,len(trump_tweets)):
        text=trump_tweets[x].text
        trump_text_tweets.append(text)

            #getting tweet id
        id=trump_tweets[x].id
        trump_tweet_id.append(id)

            #getting tweet handle 
        name=trump_tweets[x].user.screen_name
        trump_tweet_screenname.append(name)

            #getting tweet time:
        time=trump_tweets[x].created_at
        trump_tweet_time.append(time)
        
        trump="Trump"
        trump_tweet_subject.append(trump)
    

        # trump_tweets_df.to_csv("Trump_tweets_scraped.csv")
    try:
        andrews_tweets_1= twitter_api.GetSearch('dan andrews', count = 40, lang='en')

    except:
        print("there is an error")

    andrews_tweets=andrews_tweets_1

    andrews_text_tweets=[]
    andrews_tweet_id=[]
    andrews_tweet_screenname=[]
    andrews_tweet_time=[]
    andrews_tweet_subject=[]
    for x in range(0,len(andrews_tweets)):
        text=andrews_tweets[x].text
        andrews_text_tweets.append(text)

            #getting tweet id
        id=andrews_tweets[x].id
        andrews_tweet_id.append(id)

            #getting tweet handle 
        name=andrews_tweets[x].user.screen_name
        andrews_tweet_screenname.append(name)

            #getting tweet time:
        time=andrews_tweets[x].created_at
        andrews_tweet_time.append(time)
        
        andrews="Andrews"
        andrews_tweet_subject.append(andrews)

    text_tweets=trump_text_tweets+andrews_text_tweets
    tweet_id=trump_tweet_id+andrews_tweet_id
    tweet_screenname=trump_tweet_screenname+andrews_tweet_screenname
    tweet_time=trump_tweet_time+andrews_tweet_time
    tweet_subject=trump_tweet_subject+andrews_tweet_subject  

    tweets_df=pd.DataFrame({"id":tweet_id, "Created at":tweet_time, "Screen Name":tweet_screenname, "Tweet Text":text_tweets, "Subject":tweet_subject})

    tweets_df=tweets_df.drop_duplicates(subset=['Tweet Text'])


    return tweets_df        














        