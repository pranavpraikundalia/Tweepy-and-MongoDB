import pymongo
import pprint
import emoji
from operator import itemgetter
import folium
import pandas as pd
lat_long_data = pd.read_csv('states_lat_long.csv')
map_tweet = folium.Map(location=[39.50, -98.35], zoom_start=5)



from textblob import TextBlob
import re
from pymongo import MongoClient
MONGO_HOST = 'mongodb://localhost/usa_db'
client = MongoClient(MONGO_HOST)
db = client.usa_db
collection = db.usa_tweets_collection
doc_emojis= collection.find({"$or":[{"place.place_type":"city"},{"place.place_type":"neighborhood"}]},{"text":1,"extended_tweet.full_text":1,"place.full_name":1})
count=0
dict_tweet=dict()
state_per_emoji=dict()  #emoji is key
emoji_per_state=dict() #state is key
for tweet in doc_emojis:
    if 'extended_tweet' in tweet:
        analyse=tweet['extended_tweet']['full_text']
    else:
        analyse=tweet['text']
    for char in analyse:
        if char in emoji.UNICODE_EMOJI:
            count=count+1
            dict_tweet[count]=tweet
            break

for tweet_no in dict_tweet:
    state_name=dict_tweet[tweet_no]['place']['full_name'][-2:]
    if 'extended_tweet' in dict_tweet[tweet_no]:
        analyse=dict_tweet[tweet_no]['extended_tweet']['full_text']
    else:
        analyse=dict_tweet[tweet_no]['text']
    for c in analyse:
        if c in emoji.UNICODE_EMOJI:
            if state_name in emoji_per_state:
                if c in emoji_per_state[state_name]:
                    emoji_per_state[state_name][c]=emoji_per_state[state_name][c]+1
                else:
                    emoji_per_state[state_name][c] = 1
            else:
                emoji_per_state[state_name]=dict()
                emoji_per_state[state_name][c] = 1
top2_emoji=dict()
for state in emoji_per_state:
    emoji_per_state[state]=sorted(emoji_per_state[state].items(), key=itemgetter(1))[-2:]
    em2=""
    for em,cnt in emoji_per_state[state]:
        em2=em2+em
    top2_emoji[state]=em2


#print(emoji_per_state['MA'])

for each in lat_long_data.iterrows():
    if each[1]['state'] in top2_emoji:
       folium.Marker(location = [each[1]['lat'], each[1]['long']],icon=folium.Icon(color='blue'),popup=top2_emoji[each[1]['state']]).add_to(map_tweet)

map_tweet.save('map_extra.html')