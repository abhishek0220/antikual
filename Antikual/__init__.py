from flask import Flask, url_for
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import os, shutil
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
cors = CORS(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per second",]
)
api = Api(app)

@app.route('/')
def hdfd():
    return f"Running... {get_remote_address()}"

from Antikual.Resources import driveAPI
api.add_resource(driveAPI.getFiles, '/files')
