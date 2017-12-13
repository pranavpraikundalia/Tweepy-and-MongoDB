import pymongo
import pprint
import emoji

from textblob import TextBlob
from pymongo import MongoClient
MONGO_HOST = 'mongodb://localhost/twitterdb'
client = MongoClient(MONGO_HOST)
db = client.twitterdb
collection = db.twitter_search
doc_data=db.twitter_search.aggregate([{"$match":{ "$or":[{"extended_tweet.full_text": { "$regex" : '.*data.*'}},{"text": { "$regex" : '.*data.*'}}]}},{"$count":"count"}])
for tweet in doc_data:
    print("Answer 1:\nNumber of tweets with 'data' in it are : ",tweet['count'])

doc_geo=db.twitter_search.find( {"$and":[{ "$or":[{"extended_tweet.full_text": { "$regex" : '.*data.*'}},{"text": { "$regex" : '.*data.*'}}] },{"user.geo_enabled": True}]}).count()
print("\nAnswer 2:\nNumber of tweets with 'data' and geo enabled in DB are: ",doc_geo)
print("\nAnswer 3:\n\n")
doc_data_tweets=db.twitter_search.find({"$or":[{"extended_tweet.full_text": { "$regex" : '.*data.*'}},{"text": { "$regex" : '.*data.*'}}]},{"extended_tweet.full_text":1,"text":1,"_id":0})

for tweet in doc_data_tweets:
    if 'extended_tweet' in tweet:
        analyse=tweet['extended_tweet']['full_text']
    else:
        analyse=tweet['text']
    print("Tweet :",analyse)
    blob=TextBlob(analyse)
    if blob.sentiment.polarity<0:
        print("Sentiment : Negative\n")
    elif blob.sentiment.polarity>0:
        print("Sentiment : Positive\n")
    else:
        print("Sentiment : Neutral\n")