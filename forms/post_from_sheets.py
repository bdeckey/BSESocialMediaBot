# https://gspread.readthedocs.io/en/stable/#main-interface
# http://pbpython.com/pandas-google-forms-part1.html

from __future__ import print_function
import gspread
import json
import StringIO
import httplib2

from apiclient import discovery
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

from Bots.bot import uploadTwitter, uploadInstagram

# returns instance of Client after authorization
def authorize_account():
    # setup variables for reading
    SCOPE = ["https://spreadsheets.google.com/feeds"]
    SECRETS_FILE = "forms/secretKey.json"
    SPREADSHEET = "Responses"

    # Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
    # Load in the secret JSON key (must be a service account)
    json_key = json.load(open(SECRETS_FILE))
    # Authenticate using the signed key
    credentials = ServiceAccountCredentials.from_p12_keyfile_buffer(
    	json_key['client_email'], 
    	StringIO.StringIO(json_key['private_key']), 
    	scopes='https://www.googleapis.com/auth/drive')
    http = credentials.authorize(httplib2.Http())
    drive = discovery.build("drive", "v2", http=http)	

    # Client instance
    our_client = gspread.authorize(credentials)
#     our_client.login()
    return our_client

# gets all sheet ids in Client instance
# DEPRECATED
def get_spreadsheet_ids(our_client):
    sheet_id_list = []
    for sheet in our_client.openall():
        sheet_id_list.append(sheet.id)
    return sheet_id_list

# gets only sheet in Client instance
def get_spreadsheets(our_client):
    return our_client.openall()

def get_message(next_post, index = 4):
    return next_post[index]

def get_image(next_post, index = 6):
    return next_post[index]

def get_which_accts(next_post, index = 3):
    which_accts_str = next_post[3]
    return {"Twitter": "Twitter" in which_accts_str, 
           "Facebook": "Facebook" in which_accts_str,
           "Instagram": "Instagram" in which_accts_str}

def make_post(message, image, 
              which_accts = {"Twitter": True, "Facebook": True, "Instagram": True}):
    """
    Method to post message and image to desired social media accounts.
    Inputs: message, a String
            image, the filename of desired image to be posted
    """
    if which_accts.get("Twitter", False):
    	print("UPLOADING Twitter")
        uploadTwitter(image, message)
    if which_accts.get("Instagram", False):
    	print("UPLOADING INSTAGRAM")
    	print("image name: " + image)
    	print("message:" + message)
        uploadInstagram(image, message)
    # if which_accts.get("Facebook", False):
    #     print("UPLOADING Facebook")
    #     uploadFacebook(image, message) # this method doesn't exist sadly

def getImageFromURL(drive_url):
    """
    Method to download image from drive_url as the name "pic.png"
    Input: drive_url, a String representing the Google Drive location of the 
            uploaded image
    Output: filename, String of the image id with .png filetype at end (ex: "0B2XWKkYW7FwWbnNwZ1dLWVJNbWs.png")
    """

    # return None when drive_url is empty String
    if not drive_url:
        return None

    id = drive_url.split("id=")[1]

    # courtesy of https://stackoverflow.com/questions/24419188/automating-pydrive-verification-process
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    file_obj = drive.CreateFile({'id': id})
    image_name = id + ".png"
    file_obj.GetContentFile(image_name) # Download file as '<id>.png'.

    # return image name
    return image_name

if __name__ == "__main__":
	# authorize account, open spreadsheet, initialization stuff
    our_client = authorize_account()
    spreadsheet = our_client.openall()[0]
    queued_post_worksheet = spreadsheet.worksheet("Queued Responses")
    
    # get next post
    all_queued_posts = queued_post_worksheet.get_all_values()
    next_post = all_queued_posts[1]

    # get necessary info
    which_accts = get_which_accts(next_post)
    message = get_message(next_post)
    image_drive_url = get_image(next_post)
    
    # download image, set image name
    image_name = getImageFromURL(image_drive_url)

    # make post
    make_post(message, image_name, which_accts)