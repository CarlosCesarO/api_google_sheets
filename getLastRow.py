# -*- coding: utf-8 -*-
from quickstart import main
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SAMPLE_SPREADSHEET_ID = '1iw_2RWKZbwNynX50Wo-7hlvh0oQ8cV-AcwCrm6T40Mc'
SAMPLE_RANGE_NAME = 'Respostas ao formulário 1!A2:Q'

creds = main()


def getlastrow(n):
    i = 1
    list = []
    while i <= n:

        try:
                service = build('sheets', 'v4', credentials=creds)

                sheet = service.spreadsheets()
                result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range=SAMPLE_RANGE_NAME).execute()
                response = result.get('values', [])

                last_row = response[-i] if response else None
                list.append(last_row)
                

        except HttpError as err:
            print(err)

        i=i+1
        
    return list
