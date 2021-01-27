# Gossipper (Twitter Bot)
A twitter bot that performs sentiment analysis on Hashtags

1.To use Twitter the bot, you need to have Python 3 installed on your system.This bot uses tweepy module.You can install tweepy by using pip.To install tweepy, use this command :

 `$ pip install tweepy`

2.Now,you need to create a new application on Twitter. Either you can use your existing account or you can create a new one.Creating a new account for bot  is better so that your original Twitter account does not get banned.To create a new application on Twitter,open this URL in your browser :
 https://apps.twitter.com/

3.Fill all details required to create the new app.After that ,click on "Key and Access Token" tab under app settings.You will get your app's Consumer Key (API Key , Consumer Secret (API Secret) .You also need to get Access Token and Access Token Secret of your app.We will use these valuse in next step.You need to generate Access Token for first time.

4.Edit credentials.py and copy-paste  all your details carefully.

5.Now,you can run  bot.py file to run bot which will tweet sentiments ranging depending on the degree of positivity/negativity of tweets:

Tweets are classified to any of the five categories:

"Great", "Good", "Not bad", "Bad" and "Terrible"

You can run the script using the command below

 `$ python tweepy_streamer.py` 
 

6.You can also use any file instead of sample.txt . To do that,you need to open tweepy_streamer.py file and edit this line my_file=open('test.txt','r') and enter your desired filename instead of 'test.txt' .

7.Enjoy the service of Twitter Bot which tweets classifies tweets to be either "Great", "Good", "Normal", "Not bad" and "Horrible". You can also alter waiting time in script as you wish. The longer the waiting time, the more accurate the sentiment analysis is

# Twitter bot rates the sentiments on hashtags

8.Use tweepy_streamer.py file for a Twitter bot which retweet tweets based on particular hastag (script provided here use #python ),like tweets and follow the user who tweeted it. To run tweepy_streamer.py, use this command :

`$ python tweepy_streamer.py.py`

9.You can use any desired hastag(such as #javascipt ) .Just edit hastag '#python' in config.py file with whatever you want.

10. You can also edit code if you want to change how the tweets are ranked.

11.You can also deploy Twitter bot on online based servers if you want to run the bot 24 hours continously.Take care of sleep/delay if you run bot the whole day.You should try to use large sleep time so that your account does not get banned.

