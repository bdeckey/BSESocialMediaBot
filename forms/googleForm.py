from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
SECRETS_FILE = "secretKey.json"
SPREADSHEET = "Responses"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)
gc = gspread.authorize(credentials)
print("The following sheets are available")
# sh = gc.create('new_spreadsheet')
# sh.share('hearfrombruno@gmail.com', perm_type='user', role='writer')
for sheet in gc.openall():
	# if sheet.title != "Responses":
	# 	gc.del_spreadsheet(sheet.id)
	print("{} - {}".format(sheet.title, sheet.id))
sh = gc.open("Responses")
shid = sh.id
print("ID: " + shid)
sheet1 = sh.sheet1
print("Sheet1: " + str(sheet1))
print("Sheet1 title: " + sheet1.title)
worksheet = sh.get_worksheet(0)
print(worksheet)
# gc.open_by_url("https://docs.google.com/spreadsheets/d/1AX8I4ts1VPyyCDxizclkyIvVHNz1M43ae2YxZANK4pQ/edit#gid=347313902")