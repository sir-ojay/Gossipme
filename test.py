access_token='2745000907-8EEfMGkLgFtA9EVjUeuUZWMJOTfOjZUTG8FJFNj'
access_token_secret='zApWluBqmITXow8U7eKjSUbVHs0b9aGkzkgJpg3EDlO5f'
consumer_key='WML7JXu5Hty5Hft7G9xUdwhMb'
consumer_secret='r2vwB2ZL9B1BNSxKwZuYSYOdNrKbo2dqnGKR1vbuWRTgkKO8fF'

import tweepy
import re
import pandas as pd
from textblob import TextBlob

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


df = pd.DataFrame(columns = ['Tweets', 'User', 'User_statuses_count',
                             'user_followers', 'User_location', 'User_verified',
                             'fav_count', 'rt_count', 'tweet_date'])


def stream(data):
    i = 0
    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():
        print(i, end='\r')
        df.loc[i, 'Tweets'] = tweet.text
        df.loc[i, 'User'] = tweet.user.name
        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count
        df.loc[i, 'user_followers'] = tweet.user.followers_count
        df.loc[i, 'User_location'] = tweet.user.location
        df.loc[i, 'User_verified'] = tweet.user.verified
        df.loc[i, 'fav_count'] = tweet.favorite_count
        df.loc[i, 'rt_count'] = tweet.retweet_count
        df.loc[i, 'tweet_date'] = tweet.created_at
        i+=1
        if i == 200:
            break
        else:
            pass


def clean_tweet(tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity ==0:
        return 0
    else:
        return -1




stream(data = ['liverpool'])
df['clean_tweet'] = df['Tweets'].apply(lambda x: clean_tweet(x))
df['Sentiment'] = df['clean_tweet'].apply(lambda x: analyze_sentiment(x))



column=list(df['Sentiment'])
positive_tweet=[]
neutral_tweet=[]
negative_tweet=[]
for value in column:
    if value>0:
        positive_tweet.append(value)
for value in column:
    if value<0:
        negative_tweet.append(value)
for value in column:
    if value==0:
        neutral_tweet.append(value)

positive_percentile=(len(positive_tweet)/len(column))*100
neutral_percentile=(len(neutral_tweet)/len(column))*100
negative_percentile=(len(negative_tweet)/len(column))*100

print ('Postive Tweets  | Count: {} , Percent: {} %' . format(len(positive_tweet), positive_percentile))
print ('Negative Tweets | Count: {} , Percent: {} %' . format(len(negative_tweet), negative_percentile))
print ('Neutral Tweets  | Count: {} , Percent: {} %' . format(len(neutral_tweet), neutral_percentile))


