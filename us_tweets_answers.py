import pymongo
import pprint
import emoji
from operator import itemgetter

from textblob import TextBlob
import re
from pymongo import MongoClient
MONGO_HOST = 'mongodb://localhost/usa_db'
##📷🤷‍♂️\
#x='🤷'
#print(x.encode('utf-8'))
#print('🤷'.decode(encoding='UTF-8',errors='strict'))

client = MongoClient(MONGO_HOST)
db = client.usa_db
collection = db.usa_tweets_collection
#print(db.usa_tweets_collection.find().count())
#print (emoji.UNICODE_EMOJI)
#print(emoji.UNICODE_EMOJI)
#emojis=""
#for em in emoji.UNICODE_EMOJI:
#    emojis=emojis+em
#emojis= emojis.replace(' ','')
#print(emojis)
#for c in emojis:
#   if c=='📷':
#       print(c)
#regexp = re.compile(r"|".join(emojis), re.IGNORECASE)
#emojis="[\\\\x{23}\\\\x{2A}\\\\x{30}-\\\\x{39}\\\\x{A9}\\\\x{AE}\\\\x{203C}\\\\x{2049}\\\\x{2122}\\\\x{2139}\\\\x{2194}-\\\\x{2199}\\\\x{21A9}-\\\\x{21AA}\\\\x{231A}-\\\\x{231B}\\\\x{2328}\\\\x{23CF}\\\\x{23E9}-\\\\x{23F3}\\\\x{23F8}-\\\\x{23FA}\\\\x{24C2}\\\\x{25AA}-\\\\x{25AB}\\\\x{25B6}\\\\x{25C0}\\\\x{25FB}-\\\\x{25FE}\\\\x{2600}-\\\\x{2604}\\\\x{260E}\\\\x{2611}\\\\x{2614}-\\\\x{2615}\\\\x{2618}\\\\x{261D}\\\\x{2620}\\\\x{2622}-\\\\x{2623}\\\\x{2626}\\\\x{262A}\\\\x{262E}-\\\\x{262F}\\\\x{2638}-\\\\x{263A}\\\\x{2640}\\\\x{2642}\\\\x{2648}-\\\\x{2653}\\\\x{2660}\\\\x{2663}\\\\x{2665}-\\\\x{2666}\\\\x{2668}\\\\x{267B}\\\\x{267F}\\\\x{2692}-\\\\x{2697}\\\\x{2699}\\\\x{269B}-\\\\x{269C}\\\\x{26A0}-\\\\x{26A1}\\\\x{26AA}-\\\\x{26AB}\\\\x{26B0}-\\\\x{26B1}\\\\x{26BD}-\\\\x{26BE}\\\\x{26C4}-\\\\x{26C5}\\\\x{26C8}\\\\x{26CE}-\\\\x{26CF}\\\\x{26D1}\\\\x{26D3}-\\\\x{26D4}\\\\x{26E9}-\\\\x{26EA}\\\\x{26F0}-\\\\x{26F5}\\\\x{26F7}-\\\\x{26FA}\\\\x{26FD}\\\\x{2702}\\\\x{2705}\\\\x{2708}-\\\\x{270D}\\\\x{270F}\\\\x{2712}\\\\x{2714}\\\\x{2716}\\\\x{271D}\\\\x{2721}\\\\x{2728}\\\\x{2733}-\\\\x{2734}\\\\x{2744}\\\\x{2747}\\\\x{274C}\\\\x{274E}\\\\x{2753}-\\\\x{2755}\\\\x{2757}\\\\x{2763}-\\\\x{2764}\\\\x{2795}-\\\\x{2797}\\\\x{27A1}\\\\x{27B0}\\\\x{27BF}\\\\x{2934}-\\\\x{2935}\\\\x{2B05}-\\\\x{2B07}\\\\x{2B1B}-\\\\x{2B1C}\\\\x{2B50}\\\\x{2B55}\\\\x{3030}\\\\x{303D}\\\\x{3297}\\\\x{3299}\\\\x{1F004}\\\\x{1F0CF}\\\\x{1F170}-\\\\x{1F171}\\\\x{1F17E}-\\\\x{1F17F}\\\\x{1F18E}\\\\x{1F191}-\\\\x{1F19A}\\\\x{1F1E6}-\\\\x{1F1FF}\\\\x{1F201}-\\\\x{1F202}\\\\x{1F21A}\\\\x{1F22F}\\\\x{1F232}-\\\\x{1F23A}\\\\x{1F250}-\\\\x{1F251}\\\\x{1F300}-\\\\x{1F321}\\\\x{1F324}-\\\\x{1F393}\\\\x{1F396}-\\\\x{1F397}\\\\x{1F399}-\\\\x{1F39B}\\\\x{1F39E}-\\\\x{1F3F0}\\\\x{1F3F3}-\\\\x{1F3F5}\\\\x{1F3F7}-\\\\x{1F4FD}\\\\x{1F4FF}-\\\\x{1F53D}\\\\x{1F549}-\\\\x{1F54E}\\\\x{1F550}-\\\\x{1F567}\\\\x{1F56F}-\\\\x{1F570}\\\\x{1F573}-\\\\x{1F57A}\\\\x{1F587}\\\\x{1F58A}-\\\\x{1F58D}\\\\x{1F590}\\\\x{1F595}-\\\\x{1F596}\\\\x{1F5A4}-\\\\x{1F5A5}\\\\x{1F5A8}\\\\x{1F5B1}-\\\\x{1F5B2}\\\\x{1F5BC}\\\\x{1F5C2}-\\\\x{1F5C4}\\\\x{1F5D1}-\\\\x{1F5D3}\\\\x{1F5DC}-\\\\x{1F5DE}\\\\x{1F5E1}\\\\x{1F5E3}\\\\x{1F5E8}\\\\x{1F5EF}\\\\x{1F5F3}\\\\x{1F5FA}-\\\\x{1F64F}\\\\x{1F680}-\\\\x{1F6C5}\\\\x{1F6CB}-\\\\x{1F6D2}\\\\x{1F6E0}-\\\\x{1F6E5}\\\\x{1F6E9}\\\\x{1F6EB}-\\\\x{1F6EC}\\\\x{1F6F0}\\\\x{1F6F3}-\\\\x{1F6F6}\\\\x{1F910}-\\\\x{1F91E}\\\\x{1F920}-\\\\x{1F927}\\\\x{1F930}\\\\x{1F933}-\\\\x{1F93A}\\\\x{1F93C}-\\\\x{1F93E}\\\\x{1F940}-\\\\x{1F945}\\\\x{1F947}-\\\\x{1F94B}\\\\x{1F950}-\\\\x{1F95E}\\\\x{1F980}-\\\\x{1F991}\\\\x{1F9C0}]"
#doc_emojis=collection.find({"$or":[{"extended_tweet.full_text": {"$regex":'.*['+str(emojis)+']+.*'}},{"text":{"$regex":'.*[🤷📷]+.*'}}]},{"extended_tweet.full_text":1,"text":1,"_id":0})
#doc_emojis=collection.find({"extended_tweet.full_text":{"$regex": '.*['+emojis+']+.*' }},{"text":1,"_id":0})
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
            if c in state_per_emoji:
                if state_name in state_per_emoji[c]:
                    state_per_emoji[c][state_name]=state_per_emoji[c][state_name]+1
                else:
                    state_per_emoji[c][state_name] = 1
            else:
                state_per_emoji[c]=dict()
                state_per_emoji[c][state_name]=1


            if state_name in emoji_per_state:
                if c in emoji_per_state[state_name]:
                    emoji_per_state[state_name][c]=emoji_per_state[state_name][c]+1
                else:
                    emoji_per_state[state_name][c] = 1
            else:
                emoji_per_state[state_name]=dict()
                emoji_per_state[state_name][c] = 1


#for state in emoji_per_state:
#    for em in emoji_per_state[state]:
#        print(state,em,emoji_per_state[state][em])
#for states in state_per_emoji:
#    for emoji_s in state_per_emoji[states]:
#        print(states,emoji_s,emoji_per_state[states][emoji_s])
#for emoji_s in state_per_emoji:
#    for states in state_per_emoji[emoji_s]:
#        print(emoji_s,states,state_per_emoji[emoji_s][states])

emoji_count=dict()
for emo in state_per_emoji:
    count=0
    for state in state_per_emoji[emo]:
        count=count+state_per_emoji[emo][state]
    emoji_count[emo]=count
sorted(emoji_count.items(), key=itemgetter(1))

top15=sorted(emoji_count.items(), key=itemgetter(1))[-15:]
print("What are the top 15 emojis used in the entire tweets?")
print(top15[::-1])


#######

emo="🎄"
tree=dict()
tree=state_per_emoji[emo]
tree_count=[]
tree_top5=sorted(tree.items(), key=itemgetter(1))[-5:]
print("\nWhat are the top 5 states for the emoji 🎄?")
print(tree_top5[::-1])

#########

ma_emoji=emoji_per_state['MA']
ma_top5=sorted(ma_emoji.items(), key=itemgetter(1))[-5:]
print("\nWhat are the top 5 emojis for MA?")
print(ma_top5[::-1])

##########
state_count=dict()
for st in emoji_per_state:
    count=0
    for em in emoji_per_state[st]:
        count=count+emoji_per_state[st][em]
    state_count[st]=count

top5_emoji=sorted(state_count.items(), key=itemgetter(1))[-5:]
print("\nWhat are the top 5 states that use emojis?")
print(top5_emoji[::-1])


############
doc_state_count=db.usa_tweets_collection.aggregate([{"$match":{"$or":[{"place.place_type":"city"},{"place.place_type":"neighborhood"}]}},{"$project":{"state_temp":{"$split":["$place.full_name",", "]}}},{"$unwind":"$state_temp"},{ "$match":{ "state_temp":{"$regex" :'[A-Z][A-Z]' }}},{"$group" : { "_id":{"state":"$state_temp"},"count":{"$sum" : 1}}},{ "$sort" : { "count" : -1 }},{"$limit":5}])
print("\nWhat are the top 5 states that have tweets?")
for tup in doc_state_count:
    print(tup)

##########

doc_cal_city=db.usa_tweets_collection.aggregate([{"$match":{"$or":[{"place.place_type":"city"},{"place.place_type":"neighborhood"}]}},{"$project":{"state_temp":{"$split":["$place.full_name",", "]}}},{"$project":{"state_temp_1":{"$arrayElemAt":["$state_temp",0]},"state_temp_2":{"$arrayElemAt":["$state_temp",-1]}}},{"$match":{"state_temp_2":"CA"}},{"$group":{"_id":{"city":"$state_temp_1"},"count":{"$sum" : 1}}},{ "$sort" : { "count" : -1 }},{"$limit":5}])
print("\nIn the state of California, what are the top 5 cities that tweet?")
for tup in doc_cal_city:
    print(tup)






