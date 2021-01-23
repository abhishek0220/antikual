import os
cred_path = os.path.join(os.getcwd(), 'cred.json')
os.environ['CRED_PATH'] = cred_path
from Antikual import app

'''
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.discovery import build

from oauth2client.service_account import ServiceAccountCredentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'cred.json', scopes=['https://www.googleapis.com/auth/drive'])

drive_service = build('drive', 'v3', credentials=credentials)
name = input("Enter File Name : ").rstrip()
page_token = None
while True:
    response = drive_service.files().list(q=f"name contains '{name}'",
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
        print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break
'''