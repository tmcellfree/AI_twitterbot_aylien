# Import Tweepy, sleep, credentials.py
import aylien_news_api
from aylien_news_api.rest import ApiException
import tweepy
from time import sleep
from datetime import datetime
import sys
import random   # This is for using random lines in the hashtage list later on
from textblob import TextBlob
import re
from credentials import *
################################
handle = 'INSERT YOUR TWITTER HANDLE' #this is your twitter handle WITHOUT @
#################################

################################
# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
################################
# Aylien API keys
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = app_key
################################

################################
######  AYLIEN NEWS FEED  ######
################################

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

#  Set the options you want for news collections
# See here for more info https://docs.aylien.com/newsapi/common-workflows/#real-time-monitoring
opts = {
  'title': 'Synthetic Biology',     # YOUR NEWS ITEM HERE
  'categories_taxonomy': 'iab-qag', # This is a science tag SEE https://iptc.org/standards/subject-codes/
  'categories_id': ['IAB15'],       # See HERE for codes https://developers.mopub.com/docs/ui/marketplace/iab-category-blocking/
  'sort_by': 'social_shares_count.facebook',   # You can select a differnt one if you prefer
  'language': ['en'],
  'not_language': ['es', 'it'],
  'published_at_start': 'NOW-7DAYS',
  'published_at_end': 'NOW',
}

try:
    # List stories
    api_response = api_instance.list_stories(**opts)
    print("API called successfully. Returned data: ")
    print("========================================")
    news_stories = []
    for story in api_response.stories:
        if isinstance(story.title, str):
            news_piece = story.title + " via " + story.source.name + " from " + story.links.permalink
	    if story.title not in news_stories:
		news_stories.append(news_piece)
	        #print("[+] ADDING news piece to list: " + news_piece)
	# It can throw errors if there is an unrecognised symbol.. This helps prevent that
	elif isinstance(story.title, unicode):   
	    print("[+] IGNORING unicode")
	    #print(story.title.decode('ascii'))
except ApiException as e:
    print("[+] ERROR Exception when calling DefaultApi->list_stories: %sn" % e)

###################################
######   POST ON TWITTER    #######
###################################
# Avoid retweeting the same story
for i in range(len(news_stories)):
    if news_stories[i] in open("already_tweeted.txt",'r').read():
        print("[+] ALREADY TWEETED " + news_stories[i])
        i += 1
    else:
        print("[+] TWEETING " + news_stories[i] + "   >> Tweet generated using aylien newsAPI")
        api.update_status(news_stories[i] + "   >> Tweet generated using aylien newsAPI")
        print("[+] Just Tweeted!")
        open("already_tweeted.txt",'a').write(news_stories[i])
       # You only want to tweet once
	break     # Exit the loop
####################################

# NOTE: You could also use random.choice(news_stories) to select a random story
# news_stories[0] will print the most popular story based on facebook likes (you can change that to other media channels)
