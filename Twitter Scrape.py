import tweepy
import pandas as pd

# API key and Access Token
api_key = 'api_key'
api_key_secret = 'api_key_secret'

access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Authentication

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)  # To authenticate app

public_tweets = api.home_timeline()
# print(public_tweets)  # print all homepage tweets

# print(public_tweets[0].text)  # print first tweet only

# print(public_tweets[0].created_at)  # print timing of tweets

# print(public_tweets[0].user.name)  # print username

data = []   # create empty list to store all data
col = ['Time', 'User', 'Tweet']

for tweet in public_tweets:
    print(tweet.text)   # print all tweets
    print(tweet.created_at)  # print timing for tweets
    print(tweet.user.name)   # print user name

    data.append([tweet.created_at, tweet.user.name, tweet.text])  # add data in list

print(data)  # print all data

# Save data in csv
df = pd.DataFrame(data, columns=col)
# print(df)
df.to_csv('tweets.csv', index=False)
