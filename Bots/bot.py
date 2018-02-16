#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Importing directories
import tweepy, time, sys, facebook
from credentials import *
from InstagramAPI import InstagramAPI

# Creating User Authentification for Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# Creating User Authentification for Instagram
# user, pwd = 'user', 'pass'
InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login


# Creating User Authentification for Facebook
cfg = {
    "page_id"      : page_id,  # Step 1
    "access_token" : access_token   # Step 3
}
# graph = facebook.GraphAPI(access_token=access_token, version="2.7")
graph = facebook.GraphAPI(cfg['access_token'])
# Get page token to post as the page. You can skip
# the following if you want to post as yourself.
resp = graph.get_object('me/accounts')
page_access_token = None
for page in resp['data']:
    if page['id'] == cfg['page_id']:
        page_access_token = page['access_token']
graph = facebook.GraphAPI(page_access_token)



# What the bot will tweet and post, do not use quotes
image1 = input('File: ')
message1 = input('Tell me what to say: ')

if image1 == "" :
    api.update_status(status=message1);
    graph.put_object(parent_object='me', connection_name='feed', message=message1)
else:
    # Post on Instagram
    InstagramAPI.uploadPhoto(image1, message1)
    # Post on Twitter
    api.update_with_media(image1, status=message1)
    # Post on Facebook
    with open(image1) as image_ref:
        graph.put_photo(image=image_ref, message=message1)


# tweetlist = ['First Meeting!!!', 'Went great!']
#/Users/BDeckey/Desktop/BSESocialMediaBot/Bots/Blastoff.jpg

# for line in tweetlist:
#     api.update_status(line)
#     print(line)
#     print('...')
#     time.sleep(15) # Sleep for 15 seconds
# 
# print("All done!")




