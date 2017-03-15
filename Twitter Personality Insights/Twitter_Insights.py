# Import required modules
import sys
import operator
import requests
import json
import twitter
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3 as PersonalityInsights, AlchemyLanguageV1

# PersonalityInsights Credentials & Setup
personality_insights = PersonalityInsights(
  url = "https://gateway.watsonplatform.net/personality-insights/api",
  username = "USER",
  password = "PASSWORD")

# AlchemyLanguage API Credentials (will be depreciated as of 7th April 2017)
alchemy_language = AlchemyLanguageV1(api_key = 'API_KEY')

# Twitter API Credentials & Setup
twitter_consumer_key = 'CONSUMER_KEY'
twitter_consumer_secret = 'CONSUMER_SECRET'
twitter_access_token = 'ACCESS_TOKEN'
twitter_access_secret = 'ACCESS_SECRET'
twitter_api = twitter.Api(consumer_key = twitter_consumer_key, consumer_secret = twitter_consumer_secret, access_token_key = twitter_access_token, access_token_secret = twitter_access_secret)

# Define user class for analysis
class User(object):
    
    """Set up user, assign handle to user"""
    def __init__(self, handle):
        self.handle = handle
    
    """Assign a users' tweets as a list"""
    # User.tweets() will return a list of that User's last 2000 tweets (only the text). It might pay to remove hashtags and links in future to reduce the size of the output. Change 'count' to modify how many tweets are added.
    def tweets(self):
        statuses = twitter_api.GetUserTimeline(screen_name = self.handle, count = 2000, include_rts = False)
        status_lst = []
        for status in statuses:
            if (status.lang == 'en'):
                status_lst.append(status.text)
        return status_lst
    
    """This is left over from the initial purpose of this tool, in case sentiment/emotion are required - depreciates soon"""
    # Returns a json dump of sentiment information
    def sentiment_(self):
        json_dump_s = json.dumps(alchemy_language.sentiment(text = self.tweets(),
                                                                language = 'english'), indent = 2)
        #Received error trying to use dict directly in place of dumps above, for now using this long-winded method. Likely my bad and not a bug.
        full_sentiment_dict = json.loads(json_dump_s)
        sentiment_dict = full_sentiment_dict['docSentiment']
        return sentiment_dict
    
    # Returns a json dump of emotion information
    def emotion_(self):
        json_dump_e = json.dumps(alchemy_language.emotion(text = self.tweets(),
                                                                language = 'english'), indent = 2)
        #Received error trying to use dict directly in place of dumps above, for now using this long-winded method. Likely my bad and not a bug.
        full_sentiment_dict = json.loads(json_dump_e)
        sentiment_dict = full_sentiment_dict['docEmotions']
        return sentiment_dict
    
# Define a list of twitter accounts for analysis
accounts_list = ['willkennard']

# This method is a cost-saving exercise. Rather than submitting each handle's content, it combines all of the handles' content into one behemoth string which is then sent to Watson. It will only save fractions of a penny for individual searches, but it'll be far more cost effective when running hundreds of accounts through. There is clearly room for improvement.
# Note that Watson only accepts up to 20mb inputs
def tweet_unifier(lst):
    tweets = ""
    for l in lst:
        l = User(l)
        for tweet in l.tweets():
            tweets += ' ' + tweet
    return tweets

# This returns the PersonalityInsights for all users. Outputs the raw JSON dump for now.
def personality_breakdown():
    profile_text = tweet_unifier(accounts_list)
    profile = personality_insights.profile(
        profile_text.encode(encoding='utf-8', errors='strict'),
        raw_scores=True, consumption_preferences=True)
    return(json.dumps(profile, indent=2))

# This returns the Sentiment & Emotion insights for all users. Outputs the Sentiment & Emotion sections of the JSON dump in a list for now
def sentiment_and_emotion(lst):
    for l in lst:
        l = User(l)
        return(l.sentiment_(), l.emotion_())

# Print it for now just to show outputs
print(personality_breakdown())
print(sentiment_and_emotion(accounts_list))