from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



MONGO_HOST = 'mongodb://localhost/usa_db'  # assuming you have mongoDB installed locally
# and a database called 'us_db'
#WORDS = ['#bigdata', '#datascience', '#deeplearning', '#computervision']
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)
            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.usa_db
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            # grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']
            coordinates = datajson['coordinates']
            country = datajson['place']['country_code']
            if coordinates and country == "US":
                print("Tweet collected at " + str(created_at), str(datajson['coordinates']))
                # insert the data into the mongoDB into a collection called twitter_search
                # if twitter_search doesn't exist, it will be created.
                db.usa_tweets_collection.insert(datajson)
        except Exception as e:
            print(e)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
streamer.filter(locations=[-124.848974, 24.396308, -66.885444, 49.384358])
