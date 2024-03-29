from flask_restful import Resource, reqparse, request
from flask import Response
import os, json, time, base64
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
        file_name = request.args.get('name','').strip()
        page_token = request.args.get('token',None)
        order_by = request.args.get('orderBy','name').strip()
        if(page_token != None):
            page_token = base64.b64decode(page_token.strip()).decode()
        #if(len(file_name) < 3):
         #   return Response(json.dumps({'message': 'Send atleast 3 initials'}), status=403, mimetype='application/json')
        fields_to_get = 'id,name,mimeType,webViewLink,thumbnailLink,owners(displayName,emailAddress)'
        files_resp = drive_service.files().list(
            pageSize=10,
            orderBy=order_by,
            q = f"name contains '{file_name}'",
            fields=f'nextPageToken, files({fields_to_get})',
            pageToken=page_token
            ).execute()
        return files_resp
