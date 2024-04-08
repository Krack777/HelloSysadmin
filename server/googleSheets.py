from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class Table:
    def __init__(self, account_file, spreadsheet_id):
        self.account_file = account_file
        self.spreadsheet_id = spreadsheet_id

    def read(self):
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(self.account_file, scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)
        range_name = 'A1:A1'
        result = service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        for row in rows:
            result = row[0]
        return result

    def write(self, command):
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(
            self.account_file, scopes=scopes)
        self.command = command
        service = build('sheets', 'v4', credentials=creds)
        value = [[command]]
        body = {'values': value}
        result = service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range='A1',
            valueInputOption='RAW', body=body).execute()
        return 'Done'