from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class google_api:
        
    def __init__(self, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, CREDENTIALS):

        self.SAMPLE_SPREADSHEET_ID = SAMPLE_SPREADSHEET_ID
        self.SAMPLE_RANGE_NAME     = SAMPLE_RANGE_NAME
        
        # If modifying these scopes, delete the file google_sheets\token.json.
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    
        self.CREDENTIALS = CREDENTIALS

    def get_sheet(self):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file google_sheets\token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDENTIALS, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        # Instancia a conexao com a planilha do Google Sheets
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        result = sheet.values().get(
            spreadsheetId = self.SAMPLE_SPREADSHEET_ID,
            range         = self.SAMPLE_RANGE_NAME
            ).execute()

        values = result.get('values', [])

        return values