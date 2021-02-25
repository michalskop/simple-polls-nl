"""My function with gsheets."""

import gspread


""" Copies teplate from another spreadsheet to a new one - with names and first rows."""
def copy_teplate(sheet_from, sheet_to):
    from_list = sheet_from.worksheets()
    to_list = sheet_to.worksheets()
    
    i = 0
    for s in from_list:
        # set name or create a new worksheet with the name
        if i == 0:
            sheet_to.get_worksheet(0).update_title(s.title)
        else:
            sheet_to.add_worksheet(title=s.title, rows=100, cols=26)
        # copy the first line
        ws_from = sheet_from.worksheet(s.title)
        ws_to = sheet_to.worksheet(s.title)
        ws_to.insert_row(ws_from.row_values(1), 1)

        i += 1        
