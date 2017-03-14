# Import required modules
import sys
import operator
import requests
import json
import twitter
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights, AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='API_KEY')

# Twitter API Credentials
twitter_consumer_key = 'CONSUMER_KEY'
twitter_consumer_secret = 'CONSUMER_SECRET'
twitter_access_token = 'ACCESS_TOKEN'
twitter_access_secret = 'ACCESS_SECRET'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


# Define user class for future use
class User(object):
    
    """Return user personality insights based on Twitter content as evaluated by Watson's Personality Insights module"""
    
    def __init__(self, handle):
        self.handle = handle
    
    def user_tweets(self):
        statuses = twitter_api.GetUserTimeline(screen_name=self.handle, count=2000, include_rts=False)
        text = ""
        for status in statuses:
            if (status.lang =='en'):
                text += status.text
        return text

# Create User
user_one = User('USER_NAME')

# Just checking it works for now.
sentiment_json = json.dumps(alchemy_language.sentiment(text = user_one.user_tweets(),
                                                                language='english'), indent=2)

emotion_json = json.dumps(alchemy_language.emotion(text = user_one.user_tweets(),
                                                                language='english'), indent=2)


print(sentiment_json)
print(emotion_json)