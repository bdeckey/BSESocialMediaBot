#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Importing directories
import tweepy, time, sys
from credentials import *
from InstagramAPI import InstagramAPI

# Creating User for Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# Creating User for Instagram
# user, pwd = 'user', 'pass'
InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login


# What the bot will tweet and post.
image1 = input('File: ')
message = input('Tell me what to say: ')

if image1 == "" :

# Post on Instagram
InstagramAPI.uploadPhoto(image1, message)


# Post on Twitter
api.update_with_media(image1, status=message)


# tweetlist = ['First Meeting!!!', 'Went great!']


# for line in tweetlist:
#     api.update_status(line)
#     print(line)
#     print('...')
#     time.sleep(15) # Sleep for 15 seconds
# 
# print("All done!")




