# Import Tweepy, sys, sleep, credentials.py
try:
	import json
except ImportError:
	import simplejson as json
import tweepy, sys
from time import sleep
import config
import sys
# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('' , '')
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth, timeout=2000)

# Assign coordinates to the variable
city = sys.argv[1]

if city=='san_francisco':
	box = [-122.5211,37.7130,-122.3540,37.8151]
elif city== 'paris':
	box = [2.2110,48.7870,2.4678,48.9455] # paris
elif city=='munich':
	box = [11.2699,47.9798,11.8556,48.2987] # munich
else:
	raise("Enter a valid city")
 # sanfrancisco

#

# initialize blank list to contain tweets
tweets = []
# file name that you want to open is the second argument
save_file = open('../data/'+city+'.json', 'a')

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api=None):
		super(MyStreamListener, self).__init__()
		self.counter = 0
		self.list_of_tweets = tweets

	def on_status(self, status):
		record = {'Text': status.text, 'Coordinates': status.coordinates, 'Created At': status.created_at}
		self.counter += 1
		print(record)
		return True
		# if self.counter <= 1000:
		# 	print(record)
		# 	return True
		# else:
		# 	return False

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False
	
	def on_data(self, tweet):
		self.list_of_tweets.append(json.loads(tweet))
		print(tweet)
		save_file.write(str(tweet))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(api.auth, listener=myStreamListener)
myStream.filter(locations=box, is_async=True)
print(myStream)