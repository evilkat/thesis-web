#import TextBlob
from textblob import TextBlob

def computeSentiment(count,neg,pos,neut,timestamptweet,sentence_text,rtc,fc,mention,irt):
    blob = TextBlob(sentence_text)
    #print(blob.tags)
    #print(blob.noun_phrases)
    if blob.sentiment.polarity > 0.0 or blob.sentiment.subjectivity > 0.0:
        #print(timestamptweet,'retweet count: ',rtc,'favorite_count: ',fc,'Mention count: ',mention,'is_retweeted: ',irt)
        #print(blob.sentiment.polarity)
        #print(blob.sentiment.subjectivity)
        count = count + 1
        
        if blob.sentiment.polarity == 0.0:
            neut = neut + 1
            #print("Neutral")

        elif blob.sentiment.polarity < 0:
                neg = neg + 1
                #print("Negative")
        else:
                pos = pos + 1

    return count,neg,pos,neut,
        #print(blob.noun_phrases)
