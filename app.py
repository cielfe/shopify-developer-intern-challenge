
from flask import Flask, render_template, request,redirect, url_for
from werkzeug.utils import secure_filename
from flask_restful import Api
from flask_cors import CORS #allows for cross-origin requests

import functionlib.globalVariables as globals
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
#configure the web application
app.config['UPLOAD_FOLDER'] = globals.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = globals.MAX_CONTENT_LENGTH

#setup the image repository apis
api = Api(app,errors=errors)
CORS(app)
initialize_routes(api)



@app.route("/")
def home():

    return {"message":"Hello from shopify-challenge app! :)"}


if  __name__ == "__main__":    
    app.run()  
