# Running the App

1. To run the app, type in python app.py in a Terminal/ Command window
2. The dropdown menu allows you to navigate between Andrews and Trump and experience key visualisations
3. The app will update when you click the button "Press to update Twitter Data " and will fetch the most recent twitter data on Trump and Daniel (real-time visualisations)
4. Data will also automatically update when you navigate the dropdown menus! eg swtiching from Andrews to Trump will give you the most up-to-date information about Trump.


# The Main directory 

It looks messy but it is important that all the files are stored there

### The Python files have the following structure

- API.py carries out the function version of Jupyter Notebook 1 
- ML.py carries out the function of the Jupyter Notebook 2
- data.py carries out the function of Jupyter Notebook 3

# Other files 
- Procfile needed for Heroku deployment
-requirements.txt lists all requirements needed and needed for deployment

-The joblib files again means that the computationally intensive machine learning process is done by the local machine rather than Heroku. This allowed the app to be deployed

## Note: The main folder may look messy, but all the files in the main directory are needed for Heroku deployment




# Additional Notes


### The Jupyter_Notebooka fodler contains the following


1. The Twitter_API notebook contains API analysis for both Andrews Tweets and Trup tweets. 
Some exploratory analysis is done, however this is not extensive as this is mainly done in the other files
2. The Machine Learning Notebook contains the three Machine Learning Models that were used (Bayes, Random Forest and Regression) 
It also contains the details of cleaning and vectorising the tweets. This notebook may take a while to run as there is some highly computational work being done especially in the TFIDF Vectoriser step
3. The last notebook contains cleaning and grouping the data, conducting string transformations and outputting the data to a JSON file which is then used for plotle 


### The data folder contains the following:

- All csvs used in the data analysis are in this folder, a breakdown is as follows

### FROM NOTEBOOK 1

1. The tweets_scraped dataset contains all the data from the API call on both Daniel Andrews and Trump. This is the output from Notebook one and will then be classified in the second Notebook

### FROM NOTEBOOK 2

2. The IMDB.csv dataset is the training dataset used in Notebook 2( Machine Learning )
 - This Notebook then calls in the tweets_scraped dataset(explained above) and classifies each tweet into positive and negative sentiment. This is then saved as a tweets_classified. csv

### FROM NOTEBOOK 3

2.3 This notebook calls in the tweets_classified.csv from the second Notebook
2.4 This notebooks then does a number of manipulations and the output is a json file also daved

### Front end visualisations 

1. The index.html template is in the templates folder 
2. The javascript code is contained in the static/js folder (app1.js)















        
