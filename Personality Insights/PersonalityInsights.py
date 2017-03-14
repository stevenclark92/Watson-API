import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

handle_input = input('Please input handles including @ and separated with commas: ')

handle_lst = handle_input.split(', ')

print(handle_lst)

text = ''

for handle in handle_lst:
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
    for status in statuses:
        text += str(status)

print(text)

#personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
