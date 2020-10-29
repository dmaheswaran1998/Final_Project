#Needed to successfully import as a wordcould
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from ML import ML
from twython import Twython
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
from PIL import Image
from collections import defaultdict
import json

def negative_tweets(dataset):
    negative=dataset.loc[dataset['sentiment'] == "negative", ['Tweet Text']]
    negative_list=negative["Tweet Text"].to_list()
    return negative_list


def positive_tweets(dataset):
    positive=dataset.loc[dataset['sentiment'] == "positive", ['Tweet Text']]
    positive_list=positive["Tweet Text"].to_list()
    return positive_list


def edit_tweets(trump_tweets):
    trump_tweets = ''.join(trump_tweets)
    no_links = re.sub(r'http\S+', '', trump_tweets)
    no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
    no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
    
    words = no_special_characters.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
    words = [w.lower() for w in words]
    words = [w for w in words if w not in STOPWORDS]
    
    return(words)   


def remove_name(words):
    edited_word=[]
    for word in words:
        if ('donald')not in word:
            word1=word
        if ('trump')not in word1:
            edited_word.append(word1)
    return edited_word       


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


    trump_negative_list=negative_tweets(trump2)
    trump_positive_list=positive_tweets(trump2)

    positive1=edit_tweets(trump_positive_list)
    positive2=remove_name(positive1)

    sentiment = trump2.groupby("sentiment")["Frequency"].count()
    total_sentiment=trump2["sentiment"].count()
    percentage_sentiment=((sentiment/total_sentiment)*100).round()

    percentage_dict=percentage_sentiment.to_dict()
    json_list.append(percentage_dict)

    frequent_twitters=sentiment = trump2.groupby("Screen Name")["Frequency"].count()

    frequent_twitters=pd.DataFrame(frequent_twitters)
    frequency_sort=frequent_twitters.sort_values(by='Frequency', ascending=False).head(50)
    frequent_users=pd.DataFrame(frequency_sort.loc[frequency_sort["Frequency"]>1,])

    #editing the time column string and converting it into date and time
    frequent_users=frequent_users.to_dict('dict')
    json_list.append(frequent_users)

    return json_list    

































    



