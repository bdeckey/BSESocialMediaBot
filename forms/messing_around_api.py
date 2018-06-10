# https://gspread.readthedocs.io/en/stable/#main-interface
# http://pbpython.com/pandas-google-forms-part1.html

from __future__ import print_function
import gspread
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from Bots.bot import uploadTwitter, uploadInstagram
import StringIO
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

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


# prints all sheets in Client instance
def print_spreadsheets(all_spreadsheets):
    print("The following sheets are available")
    for sheet in all_spreadsheets:
        print("{} - {}".format(sheet.title, sheet.id))

# prints every row of a worksheet
def print_worksheet(our_client, a_worksheet_id):
    response_spreadsheet = our_client.open_by_key(a_worksheet)
    worksheets_list = response_spreadsheet.worksheets()
    for row in worksheets_list[0].get_all_values():
        print_list_as_columns(row)

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
    if which_accts.get("Twitter", False):
    	print("UPLOADING Twitter")
        uploadTwitter(image, message)
    if which_accts.get("Instagram", False):
    	print("UPLOADING INSTAGRAM")
    	print("image name: " + image)
    	print("message:" + message)
        uploadInstagram(image, message)

def getImageFromURL(drive_url):
	id = drive_url.split("id=")[1]
	gauth = GoogleAuth()
	# Create local webserver which automatically handles authentication.
	gauth.LocalWebserverAuth()
	# Create GoogleDrive instance with authenticated GoogleAuth instance.
	drive = GoogleDrive(gauth)
	# Initialize GoogleDriveFile instance with file id.
	file_obj = drive.CreateFile({'id': id})
	file_obj.GetContentFile('cats.png') # Download file as 'cats.png'.

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
    getImageFromURL(image_drive_url)
    
    # set image name
    image = "cats.png"

    # make post
    make_post(message, image, which_accts)