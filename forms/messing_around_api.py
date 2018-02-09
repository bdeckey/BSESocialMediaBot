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


# gets all sheets in Client instance
def get_spreadsheet_ids(our_client):
	sheet_id_list = []
	for sheet in our_client.openall():
	    sheet_id_list.append(sheet.id)
	return sheet_id_list

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

if __name__ == "__main__":
	our_client = authorize_account()
	all_spreadsheet_ids = get_spreadsheets_id(our_client)
	# Print spreadsheet names
	print_spreadsheets(all_spreadsheets)

	# print_sheet(our_client)