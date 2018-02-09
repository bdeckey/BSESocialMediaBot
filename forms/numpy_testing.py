# https://gspread.readthedocs.io/en/stable/#main-interface
# http://pbpython.com/pandas-google-forms-part1.html

from __future__ import print_function
import gspread
#from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json
import numpy as np

# helpers

def print_list_as_columns(l):
    for entry in l:
        print(entry, "| ", end="")
    print()

# returns instance of Client after authorization
def authorize_account():
	# setup variables for reading
	SCOPE = ["https://spreadsheets.google.com/feeds"]
	SECRETS_FILE = "secretKey.json"
	SPREADSHEET = "Responses"

	# Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
	# Load in the secret JSON key (must be a service account)
	json_key = json.load(open(SECRETS_FILE))
	# Authenticate using the signed key
	credentials = SignedJwtAssertionCredentials(json_key['client_email'],
	                                            json_key['private_key'], SCOPE)

	# Client instance
	our_client = gspread.authorize(credentials)

	return our_client

# prints all sheets in Client instance
def print_spreadsheets(spreadsheet_refs_list):
	print("The following sheets are available")
	for sheet in spreadsheet_refs_list:
	    print("{} - {}".format(sheet.title, sheet.id))

# prints every row of a worksheet
def print_worksheet(a_worksheet):
	for row in a_worksheet.get_all_values():
	    print_list_as_columns(row)

if __name__ == "__main__":
	our_client = authorize_account()
	spreadsheet_refs_list = our_client.openall()
	
	# Print spreadsheet names
	print_spreadsheets(spreadsheet_refs_list)

	response_spreadsheet_ref = spreadsheet_refs_list[0]
	worksheet_ref = response_spreadsheet_ref.sheet1
	print_worksheet(worksheet_ref)
	worksheet_array = np.array(worksheet_ref.get_all_values())
	print(worksheet_array)

	print(worksheet_array.shape)

	## Processing steps (URGENT):
	## Determine what platforms to post to
	## Extract the text that's going to be posted
	## Verify who is posting
	##	--> if unverified, move to unverified
	##  --> else if last_post > __ minutes then post + move to posted
	## 
	## Processing steps (less urgent):
	## Make 3 worksheets: pending, unverified, posted
	## After posting, move to posted
	## Return: Dict {String caption: ..., 
	##				 String filename: ..., 
	## 				 Dict {Twitter: boolean, Instagram: boolean, Facebook: boolean}}