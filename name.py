import tweepy
import time

consumer_key = "UT1rykKHHhGI3dLz2V8J8nv8K"
consumer_secret = "lw1tA0MI4EbNid8ICXDyRAl7XvPEUl6EwLKHp0xm575JWEc3va"
bearerKey = r"AAAAAAAAAAAAAAAAAAAAALtPnAEAAAAAUVKKz%2FgO02bOqq%2BM4lWmn2QKRJM%3DEeXoUS9NSZrdILNqK5dkDY1tHtOpl2mHlDNl19jIkKd5wUfpmY"
token = "1392930482690695170-c8xChJ4HxlUYO6KAaMfsRDm7iCSH2t"
tokenSecret = "vDE6tax16yr5Zvc3LvUIpnWrTU9LbvSwoixS1qfotLy4h"

client = tweepy.Client(
   bearerKey, consumer_key, consumer_secret,
   token, tokenSecret
)

client = tweepy.Client(bearerKey, consumer_key, consumer_secret, token, tokenSecret)



auth = tweepy.OAuth1UserHandler(bearerKey, consumer_key, consumer_secret, token, tokenSecret)
api = tweepy.API(auth)

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        #Liking the tweet
        try:
            client.like(tweet.id)
            print(tweet.text)

        except Exception as error:
            print(error)
        
        # delay between tweets
        time.sleep(1)

# Creating Stream object
stream = MyStream(bearer_token=bearerKey)

# Adding terms to search rules
stream.add_rules(tweepy.StreamRule("(#Python OR #programming) (-is:retweet -is:reply)"))

# Starting stream
stream.filter()
