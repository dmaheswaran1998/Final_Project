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

    trump=ML()

    trump2=trump[["id", "Created at", "Screen Name", "Tweet Text", "sentiment"]]
    trump2["Frequency"]=1

    #modifying the date-time string 
    time_string=trump2["Created at"].to_list()
    time_edited=[]
    for item in time_string:
        item2=item.replace(" +0000","")
        time_edited.append(item2)

    
    trump2["Created at"]=time_edited
    trump2['Created at'] =  pd.to_datetime(trump2['Created at'], infer_datetime_format=True)

    trump2['date'] = trump2['Created at'].dt.date
    #most frequent dates most are from the same day, wil lscreq axis if not all from the same day 
    date = pd.DataFrame(trump2.groupby("date")["Frequency"].count())
    date=date.sort_values(by='Frequency', ascending=False)
    #to keep majority of the graph, only display one day of data
    date=date.head(1)
    day=date.index.values[0]


    edited_time_df=trump2.loc[trump2["date"]==day, ["date", "Created at", "Screen Name", "Tweet Text", "sentiment", "Frequency"]]
    edited=edited_time_df.sort_values(by='Created at')
    edited=edited.rename(columns={"Created at": "datetime"})
    edited=edited.drop(columns=['date'])

    #json positive sentiment
    only_positive = edited.loc[edited["sentiment"] == "positive", :]
    positive_frequency=only_positive[["datetime", "Frequency"]]
    only_positive=positive_frequency.resample('0.05T', on='datetime').sum()
    only_positive=only_positive.reset_index()
    only_positive["sentiment"]="positive"


    #json negative sentiment
    only_negative = edited.loc[edited["sentiment"] == "negative", :]
    negative_frequency=only_negative[["datetime", "Frequency"]]
    only_negative=negative_frequency.resample('0.05T', on='datetime').sum()
    only_negative=only_negative.reset_index()
    only_negative["sentiment"]="negative"

    frames=[only_positive, only_negative]
    sentiment_concat=pd.concat(frames)
    sentiment_concat['datetime']=sentiment_concat['datetime'].astype(str)

    sentiment_group = sentiment_concat.groupby(['sentiment', "datetime"])
    sentiment_group_2=pd.DataFrame(sentiment_group["Frequency"].sum())
    sentiment_group_2

    results1 = defaultdict(lambda: defaultdict(dict))

    for index, value in sentiment_group_2.itertuples():
        for i, key in enumerate(index):
            if i == 0:
                nested = results1[key]
            elif i == len(index) - 1:
                nested[key] = value
            else:
                nested = nested[key] 

    json_list.append(results1)

    sentiment = trump2.groupby("sentiment")["Frequency"].count()
    total_sentiment=trump2["sentiment"].count()
    percentage_sentiment=((sentiment/total_sentiment)*100).round()

    percentage_dict=percentage_sentiment.to_dict()
    json_list.append(percentage_dict)

    example=trump2.head(5)

    screen_name=example["Screen Name"].to_list()
    tweet_text=example["Tweet Text"].to_list()

    res = {screen_name[i]: tweet_text[i] for i in range(len(screen_name))}

    trump_dict={"trump_tweets":res}

    json_list.append(trump_dict)

    return json_list    
































    



