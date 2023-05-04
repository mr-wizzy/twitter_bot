import tweepy

consumer_key = "UT1rykKHHhGI3dLz2V8J8nv8K"
consumer_secret = "lw1tA0MI4EbNid8ICXDyRAl7XvPEUl6EwLKHp0xm575JWEc3va"
bearerKey ="AAAAAAAAAAAAAAAAAAAAALtPnAEAAAAAUVKKz%2FgO02bOqq%2BM4lWmn2QKRJM%3DEeXoUS9NSZrdILNqK5dkDY1tHtOpl2mHlDNl19jIkKd5wUfpmY"
token = "1392930482690695170-c8xChJ4HxlUYO6KAaMfsRDm7iCSH2t"
tokenSecret = "vDE6tax16yr5Zvc3LvUIpnWrTU9LbvSwoixS1qfotLy4h"

client = tweepy.Client(
   bearerKey, consumer_key, consumer_secret,
   token, tokenSecret
)

auth = tweepy.OAuth1UserHandler(
    bearerKey, consumer_key, consumer_secret,
   token, tokenSecret
)
api = tweepy.API(auth)
#api = tweepy.API(client)

client.create_tweet("HeyI It's 22:37pm in Nigeria.")


print("The bot is working")
