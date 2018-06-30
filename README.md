# BSESocialMediaBot

# Libraries:
Instagram-python-API 
Tweepy 
Facebook Graph API 
gspread 
oauth2client 
pandas 
json 
pyopenssl
pydrive

Checklist to download:
- pip install -e git+https://github.com/LevPasha/Instagram-API-python.git#egg=InstagramAPI
- in python, import imageio, and run imageio.plugins.ffmpeg.download()
- pip install tweepy
- Also check out requirements.txt. While not everything there is actually needed, it may help with finding correct versions of things if you run into setup errors.

# Description:
This program will allow community contribution to social media accounts without the need of spreading passwords and usernames across a large number of people.
Using googleforms, Instagram, Twitter, and Facebook API's this bot will be able to hold a queue of posts and incrementally post them according to admin designated times. 

# How to run:
At the moment, go in the root directory of this repo and run `python -m forms.post_from_sheets`. This will post to both Twitter and Instagram the most recent submission to the Google Form.

There's a good chance that at some point auth errors might occur.

#TODOs:
1. Actually figuring out auth.
2. Make posting to Facebook work.
3. Move posts to the "Posted" sheet.
4. Move all this to work on a server.
5. Clean up stuff/catch possible exceptions, etc.

