import tweepy
import csv
import re
import config
# # OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

if __name__ == "__main__":

	# public_tweets = api.home_timeline()
	#for tweet in public_tweets:
	#    print(tweet.text)

	# status = "Testing!"
	# api.update_status(status=status)

	# Search by user name 
	# csvFile = open('data/ID.csv', 'a')
	# #Use csv Writer
	# csvWriter = csv.writer(csvFile)
	# users = ['curiosity_vm', 'apple']
	# for user_name in users:
	# 	user = api.get_user(screen_name = user_name)
	# 	csvWriter.writerow([user.screen_name, user.id, user.followers_count, user.description.encode('utf-8')])
	# 	print(user.id)
	# csvFile.close()

	parse_list = ['mobility', 'transport']
	mega_tweet_list = []
	for sname in parse_list:
		count = 0
		try:
			user_tweets = api.user_timeline(screen_name = sname, tweet_mode = 'extended', lang='en', count=100, include_rts=True)
		except tweepy.error.TweepError:
			print("Failed to run the command on that user, Skipping...")
			continue
		#   user_tweets = tweepy.Cursor(api.user_timeline, screen_name=sname, tweet_mode = 'extended', lang='en').items(20)
		print(str(count)+" "+sname)
		for t in user_tweets:
			if hasattr(t, 'retweeted_status'):
				author = t.retweeted_status.user.screen_name
			else: author = t.user.screen_name
			user_id = t.user.id
			user_name = t.user.name
			user_screenName = t.user.screen_name
			user_text = t.full_text
			#user_text = re.sub(r"http\S+", "", user_text)
			user_text = re.sub(r'https?:\/\/.*[\r\n]*', '', user_text, flags=re.MULTILINE) 
			user_text.replace("\n"," ").replace("\r"," ").replace("|"," ").replace(" | "," ").replace("?"," ")
			user_text = ' '.join(user_text.split())
			user_timestamp = t.created_at
			user_retweet = t.retweet_count
			user_favorite = t.favorite_count
			userframe = [user_id,user_name,user_screenName, author,user_text,user_timestamp,user_retweet,user_favorite]
			mega_tweet_list.append(userframe)
		count=count+1

		print(mega_tweet_list)
