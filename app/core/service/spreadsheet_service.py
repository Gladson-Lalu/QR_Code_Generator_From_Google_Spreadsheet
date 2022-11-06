import gspread
import os


class Spreadsheet:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id
        self.gc = gspread.service_account(filename=os.path.join(
            os.path.dirname(__file__), 'credentials.json'))
        self.spreadsheet = self.gc.open_by_key(self.spreadsheet_id)

    def get_route_urls(self, worksheet_name, routesColName):
        worksheet = self.spreadsheet.worksheet(worksheet_name)
        headers = worksheet.row_values(1)
        routesColIndex = headers.index(routesColName) + 1
        return worksheet.col_values(routesColIndex)
