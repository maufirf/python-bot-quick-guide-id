import tweepy

from key_loader import TWITTER_KEYS as KEYS

auth = tweepy.OAuthHandler(KEYS.API_KEY.value, KEYS.API_SECRET.value)
auth.set_access_token(KEYS.ACCESS_TOKEN.value, KEYS.ACCESS_TOKEN_SECRET.value)
api = tweepy.API(auth)

twitter_response = api.update_status("Hello world!")
print(twitter_response)