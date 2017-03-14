import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

#Place your API Key below - you can obtain one free for 30 days on the IBM Bluemix website
alchemy_language = AlchemyLanguageV1(api_key='API KEY')

#Basic inputs for now. Planning to add rudimentary support for CSV input.
base_text = input("Please define base text for sentiment & emotion analysis: ")
#Text input as a comma delimited string
base_targets_delim = input("Please input target words separated by commas: ")

#Check input string looks OK, will remove in prod.
print(base_targets_delim)

#Split string at each comma to pass through keywords correctly.
base_targets_lst = base_targets_delim.split(', ')

#Double check the list looks OK
print(base_targets_lst)    

#Sentiment analysis: This passes the text and keyword list from above to the Watson API and returns sentiment on a binary scale of Positive/Negative
sentiment_json = json.dumps(alchemy_language.targeted_sentiment(text = base_text,
                                        targets = base_targets_lst,
                                        language='english'), indent=2)

#Emotion analysis: This passes the text and keyword list from above to the Watson API and returns an emotional breakdown of the inputs
emotion_json = json.dumps(alchemy_language.targeted_emotion(text = base_text,
                                                            targets = base_targets_lst,
                                                            language='english'), indent=2)
print(sentiment_json)
print(emotion_json)