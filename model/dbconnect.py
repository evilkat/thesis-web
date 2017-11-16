from pymongo import MongoClient
import pymongo
import json
import datetime
import time

def connect(datatweet):
    try:
        client = pymongo.MongoClient("localhost",27017)
        db = client['twitterdata_clean']
        collection = db['apple']

        #tweet = json.dumps((datatweet))
        tweet = json.loads(datatweet)
        '''
        #print(tweet['created_at'],tweet['id'],tweet['quote_count'],tweet['retweet_count'],tweet['favorite_count'],tweet['entities']['user_mentions'],tweet['reply_count'],
            "text\n\n",tweet['text'],tweet['entities']['hashtags'],
            tweet['user']['name'],tweet['user']['id'],tweet['is_quote_status']
            ,tweet['favorited'],tweet['retweeted']
            )
        '''
        if 'created_at' in tweet:
            collection.insert([{'created_at':tweet['created_at'],'tweet_id': tweet['id'],'quote_count':tweet['quote_count'],'retweet_count':tweet['retweet_count'],'favorite_count':tweet['favorite_count'],'user_mentions':tweet['entities']['user_mentions'],'reply_count':tweet['reply_count'],'text':tweet['text'],'hashtags':tweet['entities']['hashtags'],'username':tweet['user']['name'],'user_id':tweet['user']['id'],'is_quoted_status':tweet['is_quote_status'],
                            'is_favorited':tweet['favorited'],'is_retweeted':tweet['retweeted']}])
        
        return True
    except BaseException as e:
        print('Failed on Data ',str(e))
        time.sleep(5)
        pass
        exit()
