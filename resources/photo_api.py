from flask import Response,request
from flask_restful import Resource
import json
import os

from functionlib import globalVariables as globals

#this class is for accessing all the photos in the uploads folder
class PhotosApi(Resource):
    def get(self):
        photo_names = {}
        directories = []
        upload_root_dir = True
        for dir in os.walk(globals.UPLOAD_FOLDER):
            #if the root directory is accessed, get the subdirectories which are the collection names
            if upload_root_dir:
                directories = dir[1]
                upload_root_dir = False
                photo_names["home"] = dir[2]
            #we are accessing the collections
            else:
                sub_dir_start_idx =  dir[0].rindex('\\')+1
                collection_name = dir[0][sub_dir_start_idx:]
                photo_names[collection_name] = dir[2]
            

        result = json.dumps(photo_names)

        return Response(result,mimetype="application/json",status=200)
    def post(self):
        file_to_upload = request.args.get('photos')
        
        result = json.dumps({"message":"user uploaded "+file_to_upload})
        return Response(result,mimetype="application/json",status=201)


class PhotoApi(Resource):
    def get(self,name):
        result = json.dumps({"message":"get single photo "+name})
        return Response(result,mimetype="application/json",status=200)
    