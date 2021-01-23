from flask_restful import Resource, reqparse, request
from flask import Response
import os, json, time, uuid
from flask_limiter.util import get_remote_address
from Antikual import limiter

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(
            os.environ['CRED_PATH'], scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)

class getFiles(Resource):
    decorators = [
        limiter.limit("5/second", key_func=get_remote_address, methods=["GET"])
    ]
    def get(self):
        return drive_service.files().list(
            fields='nextPageToken, files(id, name)'
            ).execute()