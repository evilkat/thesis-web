from model import sentiment
#import sentiment
import pymongo
from pymongo import MongoClient
import re

def cleanData(count,neg,pos,neut,timestamptweet,textvalue,rtc,fc,mention,irt):
    #pattern = re.compile('\w+')
    #msg = pattern.search(pattern,textvalue)
    msg=re.sub(r'[^\w]'," ",textvalue)
    #print(msg)
    count=sentiment.computeSentiment(count,neg,pos,neut,timestamptweet,msg,rtc,fc,mention,irt)
    return count

def getData(name,searchdate,searchyear):
    client = pymongo.MongoClient("localhost",27017)
    db = client['twitterdata_clean']
    collection = db[name]
    result = collection.find()
    count = 0
    neg = 0
    pos = 0
    neut = 0
    reg_date = '('+searchdate+')*('+ searchyear +')'
    print(reg_date)
    for obj in collection.find({'created_at':{'$regex':reg_date}}):
        #print(obj['created_at'],obj['geo'])
        if 'created_at' in obj.keys():
            count,neg,pos,neut=cleanData(count,neg,pos,neut,obj['created_at'],obj['text'],obj['retweet_count'],obj['favorite_count'],len(obj['user_mentions']),obj['is_retweeted'])

    print(count,neg,pos,neut)
    return count,neg,pos,neut

