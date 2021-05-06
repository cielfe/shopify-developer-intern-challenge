from flask import Response,request
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import werkzeug
import json
import os

from functionlib import globalVariables as globals
from functionlib import photoCollectionFunctions as pcFunctions
from resources.errors import CollectionNameNotUniqueError, CollectionCreationFailedError

class CollectionsApi(Resource):
    def get(self):
        result = {}
        result["collections"] = pcFunctions.getCollectionNames()

        result = json.dumps(result)

        return Response(result,mimetype="application/json",status=200)
    def post(self):
        body = request.get_json(force=True)

        new_collection_name = body['name']
       
        if not pcFunctions.isCollectionUnique(new_collection_name):
            raise CollectionNameNotUniqueError

        collection_path = globals.UPLOAD_FOLDER+"/"+new_collection_name
        try:
            if not os.path.exists(collection_path):
                os.makedirs(collection_path)
            result = json.dumps({"message":"${} collection created successfully".format(new_collection_name)})
        except OSError:
            raise CollectionCreationFailedError

        return Response(result,mimetype="application/json",status=201)
