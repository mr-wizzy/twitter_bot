import tweepy

consumer_key = "UT1rykKHHhGI3dLz2V8J8nv8K"
consumer_secret = "lw1tA0MI4EbNid8ICXDyRAl7XvPEUl6EwLKHp0xm575JWEc3va"
token = "1392930482690695170-c8xChJ4HxlUYO6KAaMfsRDm7iCSH2t"
tokenSecret = "vDE6tax16yr5Zvc3LvUIpnWrTU9LbvSwoixS1qfotLy4h"

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret,
   token, tokenSecret
)
api = tweepy.API(auth)
api.update_status("HeyI IT's 22:37pm in Nigeria.😁")
print("The bot is working")
