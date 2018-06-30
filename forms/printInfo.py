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