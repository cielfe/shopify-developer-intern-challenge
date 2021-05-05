from werkzeug.exceptions import HTTPException
from jwt.exceptions import ExpiredSignatureError

class NoFileSelectedError(HTTPException):
    pass
class FileTooLargeError(HTTPException):
    pass
errors ={
    "NoFileSelectedError":{
        "message":"No file was selected",
        "status": 400
    },
    "FileTooLargeError":{
        "message":"The file was too large to upload",
        "status":400
    }
}