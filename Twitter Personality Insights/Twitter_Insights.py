# Import required modules
import sys
import operator
import requests
import json
import twitter
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights, AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key = 'API_KEY')

# Twitter API Credentials
twitter_consumer_key = 'CONSUMER_KEY'
twitter_consumer_secret = 'CONSUMER_SECRET'
twitter_access_token = 'ACCESS_TOKEN'
twitter_access_secret = 'ACCESS_SECRET'

twitter_api = twitter.Api(consumer_key = twitter_consumer_key, consumer_secret = twitter_consumer_secret, access_token_key = twitter_access_token, access_token_secret = twitter_access_secret)


# Define user class for future use
class User(object):
    
    """Return user personality insights based on Twitter content as evaluated by Watson's Personality Insights module"""
    
    def __init__(self, handle):
        self.handle = handle
    
    def tweets(self):
        statuses = twitter_api.GetUserTimeline(screen_name = self.handle, count = 2000, include_rts = False)
        status_lst = []
        for status in statuses:
            if (status.lang == 'en'):
                status_lst.append(status.text)
        return status_lst

    def sentiment_json(self):
        return json.dumps(alchemy_language.sentiment(text = self.tweets(),
                                                                language = 'english'), indent = 2)

    def emotion_json(self):
        return json.dumps(alchemy_language.emotion(text = self.tweets(),
                                                                language = 'english'), indent = 2)

    def sentiment_values(self):
        full_sentiment_dict = json.loads(self.sentiment_json())
        sentiment_dict = full_sentiment_dict['docSentiment']
        return sentiment_dict

    def emotion_values(self):
        full_emotion_dict = json.loads(self.emotion_json())
        emotion_dict = full_emotion_dict['docEmotions']
        return emotion_dict

# Create User
#user_one = User('NAME')

accounts_list = ['accountOne', 'accountTwo', 'adNauseum']

def sentiment_and_emotion(lst):
    for l in lst:
        l = User(l)
        return l.sentiment_values(), l.emotion_values()

print sentiment_and_emotion(accounts_list)