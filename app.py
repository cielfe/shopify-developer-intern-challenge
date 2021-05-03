
from flask import Flask, render_template, request,redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file_ext(filename):
    
    if filename.index('.') == -1:
        return False
    file_ext_start_idx = filename.index('.') + 1
    print("filename[file_ext_start_idx:]   ", filename[file_ext_start_idx:]  )
    return filename[file_ext_start_idx:] in ALLOWED_EXTENSIONS

@app.route("/")
def home():

    return render_template('index.html',h=allowed_file_ext("hello.png"))


if  __name__ == "__main__":    
    
    app.run()  
