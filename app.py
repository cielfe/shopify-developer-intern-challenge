
from flask import Flask, render_template, request,redirect, url_for
from werkzeug.utils import secure_filename
from flask_restful import Api
from flask_cors import CORS #allows for cross-origin requests

import functionlib.globalVariables as globals
from resources.routes import initialize_routes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = globals.UPLOAD_FOLDER

#setup the image repository apis
api = Api(app)
CORS(app)
initialize_routes(api)

def allowed_file_ext(filename):
    
    if filename.index('.') == -1:
        return False
    file_ext_start_idx = filename.index('.') + 1
    print("filename[file_ext_start_idx:]   ", filename[file_ext_start_idx:]  )
    return filename[file_ext_start_idx:] in globals.ALLOWED_EXTENSIONS

@app.route("/")
def home():

    return {"message":"Hello from shopify-challenge app! :)"}


if  __name__ == "__main__":    
    app.run()  
