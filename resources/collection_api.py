from flask import Response,request
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import werkzeug
import json
import os

from functionlib import globalVariables as globals
from functionlib import photoCollectionFunctions as pcFunctions

class CollectionsApi(Resource):
    def get(self):
        result = {}
        result["collections"] = pcFunctions.getCollectionNames()

        result = json.dumps(result)

        return Response(result,mimetype="application/json",status=200)