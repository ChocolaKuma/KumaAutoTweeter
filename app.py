import tweepy as tweepy
import random as r
import time as t
import keys as keys


debug = False

access_token = keys.access_token
access_token_secret = keys.access_token_secret
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret

part1 = ["I feel ","I am ","It makes me ","My cat is "]
part2 = ["happy ","sad ","boggled ","chillin "]
part3 = ["to think about ","to see ","to hear ","to describe "]
part4 = ["pencils.","nature.","taxes.","iPads."]

def msgGen():
    msg = ""
    p1 = r.randint(0,3)
    p2 = r.randint(0,3)
    p3 = r.randint(0,3)
    p4 = r.randint(0,3)
    msg = part1[p1]+part2[p2]+part3[p3]+part4[p4]
    return msg
def tweetit(msg):
    if(msg != ""):
        print("Message Tweet")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        tweet = msg
        print(tweet)
        if(debug == False):
            api.update_status(tweet)
        if(debug == True):
            print("Post not uploaded due to debug mode being on")
    if(msg == ""):
        print("Error no message")


    
def main():
    onehour = 3600.00 #in seconds
    posttime = onehour
    starttime = t.time()
    while(1==1):
        CurrentTime = t.time() -starttime
        print(CurrentTime)
        if(CurrentTime >= posttime):
            msg = msgGen()
            print(msg)
            tweetit(msg)
            starttime = t.time() 
main()
