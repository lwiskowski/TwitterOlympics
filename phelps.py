import tweepy  #https://github.com/tweepy/tweepy
import csv
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager
import time

#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#credits to https://gist.github.com/yanofsky/5436496


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy


	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	with open('random_tweets.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	pass

def getHandles():
	tweet_list = []
	i = 0
	for follower in api.followers_ids('MichaelPhelps'):

		#time.sleep(60)
		if i == 1000:
			break
		print(api.get_user(follower).screen_name)
		i +=1
		#time.sleep(60)


if __name__ == '__main__':
	#pass in the username of the account you want to download
	#getHandles()
	lines = [line.rstrip('\n') for line in open('randomusers.txt')]
	#print(lines)
	for user in lines:
		print(user)
		get_all_tweets(user)
