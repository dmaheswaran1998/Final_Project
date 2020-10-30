#Needed to successfully import as a wordcould
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import defaultdict
import json
from ML import ML

def edit():
    json_list=[]
    ##trump=pd.read_csv("trump_tweets_classified.csv")

    tweets=ML()

    tweets2=tweets[["id", "Created at", "Screen Name", "Tweet Text", "sentiment", "Subject"]]
    tweets2["Frequency"]=1

    #modifying the date-time string 
    time_string=tweets2["Created at"].to_list()
    time_edited=[]
    for item in time_string:
        item2=item.replace(" +0000","")
        time_edited.append(item2)

    
    tweets2["Created at"]=time_edited
    tweets2['Created at'] =  pd.to_datetime(tweets2['Created at'], infer_datetime_format=True)

    tweets2['date'] = tweets2['Created at'].dt.date
    #most frequent dates most are from the same day, wil lscreq axis if not all from the same day 
    date = pd.DataFrame(tweets2.groupby("date")["Frequency"].count())
    date=date.sort_values(by='Frequency', ascending=False)
    #to keep majority of the graph, only display one day of data
    date=date.head(1)
    day=date.index.values[0]


    edited_time_tweets=tweets2.loc[tweets2["date"]==day, ["date", "Created at", "Screen Name", "Tweet Text", "sentiment", "Subject", "Frequency"]]
    edited_time_tweets=edited_time_tweets.dropna()
    
    edited=edited_time_tweets.sort_values(by='Created at')
    edited=edited.rename(columns={"Created at": "datetime"})
    edited=edited.drop(columns=['date'])

    #json positive sentiment
    only_positive = edited.loc[edited["sentiment"] == "positive", :]
    positive_frequency=only_positive[["datetime", "Frequency", "Subject"]]

    positive_frequency_trump=positive_frequency.loc[positive_frequency["Subject"]=="Trump", :]
    positive_frequency_andrews=positive_frequency.loc[positive_frequency["Subject"]=="Andrews", :]


    only_positive_trump=positive_frequency_trump.resample('0.05T', on='datetime').sum()
    only_positive_trump=only_positive_trump.reset_index()
    only_positive_trump["sentiment"]="positive"

    only_positive_andrews=positive_frequency_andrews.resample('1H', on='datetime').sum()
    only_positive_andrews=only_positive_andrews.reset_index()
    only_positive_andrews["sentiment"]="positive"


    #json negative sentiment
    only_negative = edited.loc[edited["sentiment"] == "negative", :]
    negative_frequency=only_negative[["datetime", "Frequency", "Subject"]]

    negative_frequency_trump=negative_frequency.loc[negative_frequency["Subject"]=="Trump", :]
    negative_frequency_andrews=negative_frequency.loc[negative_frequency["Subject"]=="Andrews", :]


    only_negative_andrews=negative_frequency_andrews.resample('1H', on='datetime').sum()
    only_negative_andrews=only_negative_andrews.reset_index()
    only_negative_andrews["sentiment"]="negative"

    only_negative_trump=negative_frequency_trump[["datetime", "Frequency"]]
    only_negative_trump=negative_frequency_trump.resample('0.05T', on='datetime').sum()
    only_negative_trump=only_negative_trump.reset_index()
    only_negative_trump["sentiment"]="negative"

    frames=[only_positive_trump, only_negative_trump]
    sentiment_concat=pd.concat(frames)
    sentiment_concat['datetime']=sentiment_concat['datetime'].astype(str)

    sentiment_group = sentiment_concat.groupby(['sentiment', "datetime"])
    sentiment_group_2=pd.DataFrame(sentiment_group["Frequency"].sum())
    

    results1 = defaultdict(lambda: defaultdict(dict))

    for index, value in sentiment_group_2.itertuples():
        for i, key in enumerate(index):
            if i == 0:
                nested = results1[key]
            elif i == len(index) - 1:
                nested[key] = value
            else:
                nested = nested[key] 


    frames=[only_positive_andrews, only_negative_andrews]
    sentiment_concat=pd.concat(frames)
    sentiment_concat['datetime']=sentiment_concat['datetime'].astype(str)

    sentiment_group = sentiment_concat.groupby(['sentiment', "datetime"])
    sentiment_group_2=pd.DataFrame(sentiment_group["Frequency"].sum())

    results2 = defaultdict(lambda: defaultdict(dict))

    for index, value in sentiment_group_2.itertuples():
        for i, key in enumerate(index):
            if i == 0:
                nested = results2[key]
            elif i == len(index) - 1:
                nested[key] = value
            else:
                nested = nested[key] 

    tweets={"Trump":results1, "Andrews":results2}

    json_list.append(tweets)

    trump2 = tweets2.loc[tweets2["Subject"] == "Trump", :]

            
    trump_sentiment = trump2.groupby(['sentiment'])["Frequency"].count()
    total_sentiment=trump2["sentiment"].count()
    percentage_sentiment_trump=((trump_sentiment/total_sentiment)*100).round()

    percentage_trump=percentage_sentiment_trump.to_dict()

    andrews2 = tweets2.loc[tweets2["Subject"] == "Andrews", :]

    andrews_sentiment = andrews2.groupby(['sentiment'])["Frequency"].count()
    total_sentiment=andrews2["sentiment"].count()
    percentage_sentiment_andrews=((andrews_sentiment/total_sentiment)*100).round()

    percentage_andrews=percentage_sentiment_andrews.to_dict()

    percentage_dict={"Trump":percentage_trump,"Andrews":percentage_andrews}

    json_list.append(percentage_dict)


    example=trump2.head(5)

    screen_name=example["Screen Name"].to_list()
    tweet_text=example["Tweet Text"].to_list()

    res = {screen_name[i]: tweet_text[i] for i in range(len(screen_name))}

    example2=andrews2.head(5)

    screen_name2=example2["Screen Name"].to_list()
    tweet_text2=example2["Tweet Text"].to_list()

    res2 = {screen_name2[i]: tweet_text2[i] for i in range(len(screen_name))}


    tweet_dict={"Trump":res,"Andrews":res2}

    json_list.append(tweet_dict)

    return json_list    
































    



