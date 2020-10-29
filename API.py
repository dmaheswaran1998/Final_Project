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
        trump_tweets_1= twitter_api.GetSearch('trump', count = 10, lang='en')
        id_1=(len(trump_tweets_1))
        id_1=trump_tweets_1[id_1-1].id

    except:
        print("there is an error")

#    second 100 tweets
#     try:
#         trump_tweets_2= twitter_api.GetSearch('trump', max_id=id_1-1, count = 100, lang='en')
#         id_2=(len(trump_tweets_2))
#         id_2=trump_tweets_2[id_2-1].id

#     except:
#         print("there is an error")     

#     third 100 tweets
#     try:
#         trump_tweets_3= twitter_api.GetSearch('trump', max_id=id_2-1, count = 100, lang='en')
#         id_3=(len(trump_tweets_3))
#         id_3=trump_tweets_3[id_3-1].id

#     except:
#         print("there is an error")    

#         fourth 100 tweets
#     try:
#         trump_tweets_4= twitter_api.GetSearch('trump', max_id=id_3-1, count = 100, lang='en')
#         id_4=(len(trump_tweets_4))
#         id_4=trump_tweets_4[id_4-1].id

#     except:
#         print("there is an error")

#         fifth 100 tweets
#     try:
#         trump_tweets_5= twitter_api.GetSearch('trump', max_id=id_4-1, count = 100, lang='en')
#         id_5=(len(trump_tweets_5))
#         id_5=trump_tweets_5[id_5-1].id

#     except:
#         print("there is an error")

#         sixth 100 tweets
#     try:
#         trump_tweets_6= twitter_api.GetSearch('trump', max_id=id_5-1, count = 100, lang='en')
#         id_6=(len(trump_tweets_6))
#         id_6=trump_tweets_5[id_6-1].id

#     except:
#         print("there is an error")

    trump_tweets=trump_tweets_1

    text_tweets=[]
    tweet_id=[]
    tweet_screenname=[]
    tweet_time=[]
    for x in range(0,len(trump_tweets)):
    #getting text language
        text=trump_tweets[x].text
        text_tweets.append(text)
        
        #getting tweet id
        id=trump_tweets[x].id
        tweet_id.append(id)
        
        #getting tweet handle 
        name=trump_tweets[x].user.screen_name
        tweet_screenname.append(name)
        
        #getting tweet time:
        time=trump_tweets[x].created_at
        tweet_time.append(time)

        trump_tweets_df=pd.DataFrame({'id': tweet_id, 'Created at' : tweet_time, 'Screen Name': tweet_screenname, "Tweet Text": text_tweets})

        #dropping tweets that have duplicate text
        trump_tweets_df=trump_tweets_df.drop_duplicates(subset=['Tweet Text'])

        # trump_tweets_df.to_csv("Trump_tweets_scraped.csv")

    return trump_tweets_df        














        