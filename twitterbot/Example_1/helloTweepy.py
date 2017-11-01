import tweepy

consumer_key = "ENoOr6P7T70NudHsf8EaiGPkC"
consumer_secret = "uXkEUKstXPklDEFEOm81ydAAIaYRDJ1MNatvZTF1jZoCVA78zX"
access_token = "924033433663426561-UxLwhGJd3AsPB1Vuy7IhvkxFAg9stPY"
access_token_secret = "8aUxmskX0jn4E1D8Xws8tZBDC8N2T78A0KDCRXZBhV8Hh"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print("Error! Failed to get request token.")


api = tweepy.API(auth)
public_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	print(tweet.text)

user = api.get_user('RIMonthly')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
	print(friend.screen_name)

api.update_status("first bot post! #bots")