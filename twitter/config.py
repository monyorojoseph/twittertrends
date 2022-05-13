from django.conf import settings
import tweepy

API_KEY = settings.API_KEY
API_KEY_SECRET =settings.API_KEY_SECRET
ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET
# twitter
# connect tweepy api
def verify_api():    
    auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET,  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except tweepy.TweepyException as exc:
        print(exc)
        return
    else:
        return api

