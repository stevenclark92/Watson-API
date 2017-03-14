# Twitter Personality Insights

Currently this tool only provides sentiment & emotion insights from AlchemyLanguage, though this was included simply to test that the tool was working correctly.

The tool takes the text from the defined user's last 2000 Tweets and uses this as a base for generating insights with Watson, currently returning average sentiment and emotion.

## To Use
Usage is simple enough, though you'll need API keys for Twitter & AlchemyLanguage, which are available from Twitter & IBM respectively. Simply add the keys, tokens and secrets in the designated places on lines 10 & 13-16 and define a user name you'd like to examine on line 38.

## To Do
Switch from AlchemyLanguage to PersonalityInsightsV2 in order to provide a better breakdown of personality & behaviour. Baby steps!
