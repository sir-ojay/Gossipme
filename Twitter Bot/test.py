
import re

import csv
import tweepy
from tweepy import OAuthHandler
#TextBlob perform simple natural language processing tasks.
#from textblob import TextBlob


access_token = "965215367860809728-nCUC1u58RG8A9UwGDsF6z0Ts86fpCfl"
access_token_secret = "SxwAvywjoyfdrfxxiLkd2DBLsDzsGeFYpG0irZz3eCi1n"
consumer_key = "B8iUI7VPsyX3C6VXz4br08BxL"
consumer_secret = "aEbKvfOubAbCEfmsh8KL7LW4VHDbkqoT2GSplMjoIpyTjl3qF8"

# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

def get_tweets(query, count = 300):

    # empty list to store parsed tweets
    tweets = []
    target = open("mytweets.txt", 'w', encoding='utf-8')
    # call twitter api to fetch tweets
    q=str(query)
    a=str(q+" sarcasm")
    b=str(q+" sarcastic")
    c=str(q+" irony")
    fetched_tweets = api.search(a, count = count)+ api.search(b, count = count)+ api.search(c, count = count)
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:

        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")
    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets
tweets = get_tweets(query ="Trump", count = 20000)