from werkzeug.exceptions import HTTPException
from jwt.exceptions import ExpiredSignatureError

class NoFileSelectedError(HTTPException):
    pass
class FileTooLargeError(HTTPException):
    pass
class PhotoNameAlreadyExistsError(HTTPException):
    pass
class CollectionNameNotUniqueError(HTTPException):
    pass
class CollectionDoesNotExistError(HTTPException):
    pass
class CollectionCreationFailedError(HTTPException):
    pass
errors ={
    "NoFileSelectedError":{
        "message":"No file was selected",
        "status": 400
    },
    "FileTooLargeError":{
        "message":"The file was too large to upload",
        "status":400
    },
    "PhotoNameAlreadyExistsError":{
        "message": "The photo cannot be added since another photo in the selected collection has the same name. Please change the name and try again.",
        "status":400
    },
    "CollectionNameNotUniqueError":{
        "message": "The collection name is not unique. Please enter a different name.",
         "status":400
    },
    "CollectionCreationFailedError":{
        "message":"The collection could not be created. Please make sure characters in name are valid",
        "status": 400
    },
    "CollectionDoesNotExistError":{
        "message": "The specified collection name does not exist. Please create it before you add photos",
        "status":400
    }
}