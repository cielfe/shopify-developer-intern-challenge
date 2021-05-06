This is Ciel Emond's submission for the "Fall 2021 - Shopify Developer Intern Challenge"

Markup : #Application Description#
My image repository is called "Ciel Gallery"

Users can do two things on this application. These actions are easily accessible at the top of the page:
    1. Create 'Collections' to organize the images you upload. Essentially, collections are the folders within the 'uploads' folder in this web application.
    2. Upload new photos to either the 'Main Gallery' or a specified collection

For any of these actions, the user will receive feedback in the readable text area below the function. They may either see a success message, error message, or warning message. 

For the error messages, the feedback includes how they can prevent the error the next time they attempt to execute an action. E.g. if one tries to add an images to a 'Collection' that does not exist, an error message will appear in the text area, "ERROR for "Paris,_France_window_view.jpg": The specified collection name does not exist. Please create one before you add photos"

Below the two create actions, the photos and collections are displayed under "Photo Gallery and Collections". The main gallery is the default place where images can be saved. The collection names are bolded and are placed above the images in that specific collection.

Markup :  #How to run the application#

Ciel Gallery is run using Flask (a Python web framework) and JavaScript. This application works best in a Chrome Browser.

Check that you have the following libraries that this web application uses. If you have them, you can skip the "pip install" of these libraries.

1.flask
2.flask_restful
3.Werkzeug* (flask should have this library installed but it is good to double check)

Go to the main folder of this project, "shopify-developer-intern-challenge", and open VS Code or a command prompt.
Execute the command "python app.py" if you have the python environment variable set up. If you have VS Code, rigth-click "app.py" in the main project directory and select "Run python file in terminal".

The Flask application is running successfully when you see the following text appear in the terminal/command prompt:

* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)