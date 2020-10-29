#Libries to process tweets 
import pandas as pd
import numpy as np
import re
import string
import nltk
nltk.download('stopwords')  
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from string import punctuation 
from API import API

#Using sk.learn Libraries to test models and then
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression

def ML():
    training_reviews=pd.read_csv("IMDB_Dataset.csv",  encoding='latin-1')

    #editing the training review column

    text = training_reviews['review'].to_list() 
    edited_text=[]

    #Lowercase tweets
    for review in text:
        #convert all letters to a lower case
        edited_review=review.lower()
    
        #removing punctuation 
        
        edited_review=re.sub("([.;:!\'?,\"()\[\]])","", edited_review)

        
        
        #removing the <br / br>
        
        edited_review=re.sub("(<br\s*/><br\s*/>)|(\-)|(\/)", " ", edited_review)
        
        edited_text.append(edited_review)

    tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
    X = tfidfconverter.fit_transform(edited_text).toarray()

    y=training_reviews['sentiment'].to_list()


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sentiment_regression_classifier=LogisticRegression()
    sentiment_regression_classifier.fit(X_train, y_train)
    linear_predictions = sentiment_regression_classifier.predict(X_test)

    trump_df=API()
    ##trump_df=pd.read_csv("Trump_tweets_scraped.csv")


    #cleaning up the trump tweets:
    trump = trump_df['Tweet Text'].to_list()
    trump_text=[]
    sentiment_list=[]

    #Lowercase tweets
    for tweet in range (0, len(trump)):
        #lower case
        #removing speocial cahracters
        edited_tweet = re.sub(r'\W', ' ', str(trump[tweet]))
    
        # remove sinflue
        edited_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', edited_tweet)
    
        # Remove single characters from the start
        edited_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', edited_tweet) 
    
        # Substituting multiple spaces with single space
        edited_tweet= re.sub(r'\s+', ' ', edited_tweet, flags=re.I)
    
        # Removing prefixed 'b'
        edited_tweet = re.sub(r'^b\s+', '', edited_tweet)
        
        #removing stopwords tweets
        
        
        edited_tweet=edited_tweet.lower()
        
        trump_text.append(edited_tweet) 
        
        sentiment_trump = sentiment_regression_classifier.predict(tfidfconverter.transform([edited_tweet]).toarray())
        sentiment_list.append(sentiment_trump)

        sentiment_list_edited=[]

    for item in sentiment_list:
        if "positive" in item:
            sentiment_list_edited.append("positive")
        else:
            sentiment_list_edited.append("negative")
    
    trump_df["sentiment"]=sentiment_list_edited

    ##trump_df.to_csv("trump_tweets_classified.csv")

    return trump_df    


        



 
 
    

        




