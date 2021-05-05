from flask import Response,request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user,get_jwt_identity,get_jwt_claims
from flask_jwt_extended.exceptions import NoAuthorizationError
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

from backend import globalVariables as globals
from backend import functions
from resources.errors import SchemaValidationError,InternalServerError,DatabaseUpdateError,NoDocumentsFoundError, UnauthorizedEndPointError, InvalidReferenceFieldValueError,DocumentDeletionError,InvalidPostRequestError, MissingRequestArgsError
##Author: Ciel Emond
##Date: March 11 2021
##Description:This file contains the API template for a single collection (not a matrix one)

#NOTE: once your APIs are completed, declare them in the "routes.py" file in the function called
#initialize_routes(api)
#change the second parameter as you see fit as long as "/api/" is at the beginning
#add the following lines
#api.add_resource(REPLACE_NAMEsApi,"/api/api_collection_name")
#api.add_resource(REPLACE_NAMEApi,"/api/api_collection_name/<id>")

#NOTE:declare the collection variables that will be used in the apis
#NOTE:assign proper collection name to "api_collection" variable
api_collection_name = ""
api_collection = globals.DB[api_collection_name] 

class REPLACE_NAMEsApi(Resource):
    @jwt_required
    def get(self):
        try:
            ##NOTE:Replace "MP_ID" with any arguments you are expecting from the request 
            search_id = request.args.get('MP_ID')
            search_id = ObjectId(search_id)
            #query the collection

            #NOTE: Use only 1 of the code blocks below for retrieving rows from your collection
            #NOTE - Code Block #1: Use this code below if you are returning more than 1 document/row in the api
            cursor = api_collection.find({"MP_ID":search_id})
            list_cursor = list(cursor)
            result = {"result":list_cursor}
            result = dumps(result)
            #NOTE - Code Block #2: Use this code below if you are only returning one single row
            result = dumps(api_collection.find({"MP_ID":search_id}).next())

            return Response(result,mimetype="application/json",status=200)
        except StopIteration:
            raise NoDocumentsFoundError

    @jwt_required
    def post(self):
        try:
            body = request.get_json(force=True)
            ##NOTE:Replace "MP_ID" with any arguments you are expecting from the request 
            body["MP_ID"] = ObjectId(body["MP_ID"])
                
            ##NOTE:optional if statement for checking if the row to be inserted is actually unique 
            if api_collection.count_documents({"MP_ID":body["MP_ID"]}) >= 1:
                raise InvalidPostRequestError

            #retrieve the document id that the current scenario's parent field id will be removed from
            #this operation must be performed in order to avoid duplicity; a new document will be created for this scenario
            old_doc_id = request.args.get('old_doc_id')
            if not old_doc_id:
                raise MissingRequestArgsError
            else:
                old_doc_id = ObjectId(old_doc_id)
            
            #NOTE: update the "api_collection" variable name if you changed the name before the class declarations
            #check if the new array_field value exists in the collection
            #there should only be one parent param array field in each collection
            #this is to help reduce changes to APIs in the future
            parent_param_array_fields = [s for s in body.keys() if s in globals.PARENT_PARAM_ARRAY_FIELDS]
            if len(parent_param_array_fields) == 1:
                array_field = parent_param_array_fields[0]
                api_collection.update_one({"_id":old_doc_id},{"$pull":{array_field: body[array_field]}})
            else:
                for array_field in parent_param_array_fields:
                    api_collection.update_one({"_id":old_doc_id},{"$pull":{array_field: body[array_field]}})

            #NOTE: depending on how many foreign key fields you have in the new row, be sure to add to the list that currently has ["MODEL_PARAMETERS"]
            #insert the new document into api_collection_name collection
            inserted_id = functions.addDocument(api_collection_name,body,["MODEL_PARAMETERS"])

            return Response(dumps({"_id":inserted_id}),mimetype="application/json",status=201)
        except KeyError:
            raise SchemaValidationError
      

class REPLACE_NAMEApi(Resource):
    @jwt_required
    def get(self,id):
        try:
            search_id = ObjectId(id)
            #query the disease params collection
            api_collection_result = dumps(api_collection.find({"_id":search_id}).next())

            return Response(api_collection_result,mimetype="application/json",status=200)
        except StopIteration:
            raise NoDocumentsFoundError

    @jwt_required
    def put(self,id):
        #NOTE: if you do not want a default_user_role (e.g. non-expert) to access the route, uncomment the code below
        # check if the user is authorized to access this endpoint
        # claims = get_jwt_claims()
        # if claims['role'] == globals.DEFAULT_USER_ROLE:
        #     raise UnauthorizedEndPointError
        try:
            #convert the id specified in URL to an ObjectId
            proper_id = ObjectId(id)

            body = request.get_json()
            body["MP_ID"] = ObjectId(body["MP_ID"])

            #NOTE: update the "api_collection" variable name if you changed the name before the class declarations   
            #NOTE: Optional if statement you can expand on to ensure no duplicate values get inserted into the collection 
            if api_collection.count_documents({"MP_ID":body["MP_ID"]}) >= 1:
                raise DatabaseUpdateError

            #NOTE: update the "api_collection" variable name if you changed the name before the class declarations
            #apply the changes
            for field in body.keys():
                edit_success = functions.editDocument(api_collection_name, "_id", proper_id, field, body[field])
                
                #if the edit could not be performed, raise exception
                if edit_success == False:
                    raise DatabaseUpdateError
            #prepare update success statement
            update_status = json.dumps({"message":"Update successful"})
            return Response(update_status,mimetype="application/json",status=200)
        except KeyError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
    @jwt_required
    def delete(self,id):
        #NOTE: if you do not want a default_user_role (e.g. non-expert) to access the route, uncomment the code below
        #check if the user is authorized to access this endpoint
        # claims = get_jwt_claims()
        # if claims['role'] == globals.DEFAULT_USER_ROLE:
        #     raise UnauthorizedEndPointError
        try:
            search_id = ObjectId(id)
           
            query = {"_id":search_id}

            #NOTE: update the "api_collection" variable name if you changed the name before the class declarations
            #check if the array for the parent param fk fields is greater than 1
            #if that is the case, just remove the id specified in the parent param field name in the request args
            #perform deletion
           
            array_field_value = api_collection.find({"_id":search_id}).next()["MP_ID"]

            if (len(array_field_value) > 1):
                #NOTE: update the "array_field" variable value depending on what 
                #your scenario foreign key is in your collection (same as the GET for REPLACE_NAMEsApi above)
                array_field = "MP_ID"
                value_to_remove = request.args.get(array_field)

                if not value_to_remove:
                    raise MissingRequestArgsError 
                value_to_remove = ObjectId(value_to_remove)
                #remove the array_field value from the document's parent param field array
                update_result = api_collection.update_one({"_id":search_id},{"$pull":{array_field: value_to_remove}})
                if (update_result.modified_count == 1):
                    delete_status = json.dumps({"message":"Deletion of {}, {}, successful".format(array_field,request.args.get(array_field)),"status":200})
                else:
                     raise DocumentDeletionError
            
            else:
                #NOTE: if your collection is referenced by other ones (the source of a set of foreign_keys)
                #use Code Block 1, 2 OR 3 accordingly

                #NOTE: Code Block 1: use this if there is only one foreign key name (e.g. SCHOOL_ID)
                #replace the last parameter in deleteDocument with the correct FK name
                delete_success = functions.deleteDocument(api_collection_name,query,"REPLACE_WITH_FK_NAME")

                #NOTE: Code Block 2: use this if the collection is NOT a foreign key source 
                # for others collections; the last parameter is an empty string
                delete_success = functions.deleteDocument(api_collection_name,query,"")

                #NOTE: Code Block 3: use this if there is more than one foreign key name (e.g. CSD_1_ID and CSD_ID)
                delete_success = functions.deleteDocumentWithMultipleFkIdNames(api_collection_name,query)
        
                #inform client if deletion could not be performed
                if delete_success == False:
                    raise DocumentDeletionError
                #prepare update success statement
                delete_status = json.dumps({"message":"Deletion successful","status":200})
            return Response(delete_status,mimetype="application/json",status=200)
                  
        except StopIteration:
            raise NoDocumentsFoundError
