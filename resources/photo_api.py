from flask import Response,request
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import werkzeug
import json
import os

from functionlib import globalVariables as globals
from resources.errors import NoFileSelectedError,FileTooLargeError



#this class is for accessing all the photos in the uploads folder
class PhotosApi(Resource):
    def get(self):
        photo_names = {}

        upload_root_dir = True
        for dir in os.walk(globals.UPLOAD_FOLDER):
            #if the root directory is accessed, get the subdirectories which are the collection names
            if upload_root_dir:
                directories = dir[1]
                upload_root_dir = False
                photo_names[globals.DEFAULT_PHOTO_LOCATION] = dir[2]
            #we are accessing the collections
            else:
                sub_dir_start_idx =  dir[0].rindex('\\')+1
                collection_name = dir[0][sub_dir_start_idx:]
                photo_names[collection_name] = dir[2]
            

        result = json.dumps(photo_names)

        return Response(result,mimetype="application/json",status=200)
    def post(self):
        try:
            file = request.files['file']

            #check if the file name is empty
            if file.filename == '' or not file:
                raise NoFileSelectedError
            #secure the file name and then save it in the upload folder
            filename = secure_filename(file.filename)
            file.save(os.path.join(globals.UPLOAD_FOLDER, filename))

            
            result = json.dumps({"message":"{} uploaded successfully".format(filename)})
            return Response(result,mimetype="application/json",status=201)
        except RequestEntityTooLarge:
            raise FileTooLargeError


class PhotoApi(Resource):
    def get(self,name):
        result = json.dumps({"message":"get single photo "+name})
        return Response(result,mimetype="application/json",status=200)
    