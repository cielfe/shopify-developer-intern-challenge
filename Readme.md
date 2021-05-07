This is Ciel Emond's submission for the "Fall 2021 - Shopify Developer Intern Challenge"

# Application Description #
My image repository is called "Ciel Gallery"

Users can do two things on this application. These actions are easily accessible at the top of the page:
1. Create 'Collections' to organize the images you upload. Essentially, collections are the folders within the 'uploads' folder in this web application.
2. Upload new photos to a specific collection (a datalist field labeled "Collection").'Main Gallery' is the default location. 

For any of these actions, the user will receive feedback in the text area below the function. They may either see a **success** message, **error** message, or **warning** message. 

For the error messages, the feedback includes how they can prevent the error the next time they attempt to execute an action. E.g. if one tries to add an images to a 'Collection' that does not exist, an error message will appear in the text area, "ERROR for "Paris_France_window_view.jpg": The specified collection name does not exist. Please create one before you add photos"

Below the two create actions, the photos and collections are displayed under "Photo Gallery and Collections". The Main Gallery is the default place where images can be saved. The collection names are bolded and are placed above the images in that specific collection.

# Application Technology Set-up #

Ciel Gallery uses Flask (a Python web framework) and JavaScript. This application works best in a Chrome Browser. If you want to use Mozilla, please increase the *"network.http.connection-timeout"* property to 6000

Check if you have the following libraries that the web application uses. If you have them, you can skip the "pip install" of these libraries.

  1. flask
  2. flask_restful
  3. Werkzeug* (flask should have this library installed but it is good to double check)


# How to run the application #

## Part 1: Start the Flask Server ##
### VS Code ###
1. Open the main folder of this project, "shopify-developer-intern-challenge", with **VS Code** 
2. Right-click "app.py" (in the main project directory) and select "Run python file in terminal" to **start the Flask server**.You should see this text in the terminal or command prompt:

*Serving Flask app "app" (lazy loading)
 *Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 *Debug mode: off
 *Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### Command Prompt ###
1. Open a terminal or command prompt in main folder of this project, "shopify-developer-intern-challenge"
2. Execute the command "python app.py" to **start the Flask server**. Only use the *python* keyword if the Python Environment Variable is set up. You should see this text in the terminal or command prompt:

*Serving Flask app "app" (lazy loading)
 *Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 *Debug mode: off
 *Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Part 2: Accesing the Application ##

1. Go the main folder of this project "shopify-developer-intern-challenge"
2. Open the *index.html* file in a Chrome or Mozilla browser. It works best in a Chrome Browser. 

# Application Test Cases #

All testcases involve manually uploading image(s) provided in the sub-folder located at "./shopify-developer-intern-challenge/testcase_sample_photos".

After executing Test cases #**1 and 2**, run the Python script "testcase_script.py" in a terminal or command prompt to verify that the actions were performed correctly. A testcase would have a status "PASS or FAIL". All these testcases will **PASS**. 

The following script output will appear in the command line:
"Test case #1: Status - PASS
Test case #2: Status - PASS"

Test cases # **3 and 4** have to be verified by reading the text box in either "Create a new photo collection" or "Upload new photos here!" They are erroneous tasks which will pass by displaying a message beginning with either "Warning" or "ERROR"

1. Upload 3 images (city-rainy-day.jpg, lanterns-on-water.jpg, and otter.jpg) to the "Main Gallery" Collection
2. Create a new collection called "Animals". Then upload "otter.jpg" and "sloth.jpg" to that new collection you created
3. Attempt to create a collection named "Vacation" (Collection names are case-sensitive). This collection already exists. 
  - **Expected message in textarea**: "ERROR: The collection name is not unique. Please enter a different name."
4. Upload any photos to the "Paris" collection, which does not exist.
  - **Expected message in text area**: "ERROR for "*placeholder*": The specified collection name does not exist. Please create it before you add photos"

# The End #
