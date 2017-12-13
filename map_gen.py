import folium
import pandas as pd
tweetdata = pd.read_csv('usa_tweets.csv')
map_tweet = folium.Map(location=[39.50, -98.35], zoom_start=5)
for each in tweetdata.iterrows():
       folium.CircleMarker(location=[each[1]['lat'], each[1]['long']],radius=5).add_to(map_tweet)

map_tweet.save('map.html')
