import tweepy
import time

consumer_key = "B8iUI7VPsyX3C6VXz4br08BxL"
consumer_secret = "aEbKvfOubAbCEfmsh8KL7LW4VHDbkqoT2GSplMjoIpyTjl3qF8"
key = "965215367860809728-nCUC1u58RG8A9UwGDsF6z0Ts86fpCfl"
secret = "SxwAvywjoyfdrfxxiLkd2DBLsDzsGeFYpG0irZz3eCi1n"
# ACCESS_TOKEN = "965215367860809728-nCUC1u58RG8A9UwGDsF6z0Ts86fpCfl"
# ACCESS_TOKEN_SECRET = "SxwAvywjoyfdrfxxiLkd2DBLsDzsGeFYpG0irZz3eCi1n"
# CONSUMER_KEY = "B8iUI7VPsyX3C6VXz4br08BxL"
# CONSUMER_SECRET = "aEbKvfOubAbCEfmsh8KL7LW4VHDbkqoT2GSplMjoIpyTjl3qF8"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

tweets = api.mentions_timeline()
FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
	file_read = open(FILE_NAME, "r")
	last_seen_id = int(file_read.read().strip())
	file_read.close()
	return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
	file_write = open(FILE_NAME, 'w')
	file_write.write(str(last_seen_id))
	file_write.close()
	return

def reply():
	tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")		
	for tweet in reversed(tweets):
		if "#mukhtaragboola" in tweet.full_text.lower():
				print("Replied To ID - " + str(tweet.id))
				api.update_status("@" + tweet.user.screen_name + " Hi, I'm here!", tweet.id)
				store_last_seen(FILE_NAME, tweet.id)

while True:
	reply()
	time.sleep(30)