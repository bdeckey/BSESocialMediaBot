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
from PIL import Image

import requests

def convertToJPG(image):
	im = Image.open(image)
	rgb_im = im.convert('RGB')
	imageJPG = image.split(".")[0] + ".jpg"
	rgb_im.save(imageJPG)
	return imageJPG

# Post on Instagram
def uploadInstagram(image, message):
	# Creating User for Instagram
	# user, pwd = 'user', 'pass'
	insta = InstagramAPI(user, pwd)
	insta.login()  # login
	if image.split(".")[1] is not "jpg":
		image = convertToJPG(image)
	insta.uploadPhoto(image, message)


# Post on Twitter
def uploadTwitter(image, message):
	# Creating User for Twitter
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_with_media(image, status=message)

# uploadInstagram("cats.jpg", "asdf")
# uploadInstagram("https://drive.google.com/open?id=0B2XWKkYW7FwWVkxKczJxYlJGbXM", "hello")
# tweetlist = ['First Meeting!!!', 'Went great!']


# for line in tweetlist:
#     api.update_status(line)
#     print(line)
#     print('...')
#     time.sleep(15) # Sleep for 15 seconds
# 
# print("All done!")




