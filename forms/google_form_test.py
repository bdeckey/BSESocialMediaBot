# https://gspread.readthedocs.io/en/stable/#main-interface
# http://pbpython.com/pandas-google-forms-part1.html

from __future__ import print_function
import gspread
#from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "secretKey.json"
SPREADSHEET = "Responses"
# Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
# Load in the secret JSON key (must be a service account)
json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)

gc = gspread.authorize(credentials)

print("The following sheets are available")

sheet_id_list = []

for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))
    sheet_id_list.append(sheet.id)

response_spreadsheet = gc.open_by_key(sheet_id_list[0])
#h ttps://stackoverflow.com/questions/33713084/download-link-for-google-spreadsheets-csv-export-with-multiple-sheets
response_csv = "https://docs.google.com/spreadsheets/d/1AX8I4ts1VPyyCDxizclkyIvVHNz1M43ae2YxZANK4pQ/gviz/tq?tqx=out:csv&sheet={sheetname}"

worksheets_list = response_spreadsheet.worksheets()

for row in worksheets_list[0].get_all_values():
    print(row)  