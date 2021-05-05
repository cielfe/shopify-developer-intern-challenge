import os

from functionlib import globalVariables as globals
def photoExistsInCollection(file_name,collection_name):
    '''This function returns a boolean value if a specific photo name already exists in the collection
        Returns True if it does, False otherwise'''
    search_dir = globals.UPLOAD_FOLDER + "/"+collection_name
    for root,dirs,files in os.walk(search_dir):
        if file_name in files:
            return True
        break
    return False

def getCollectionNames():
    collections = [globals.DEFAULT_PHOTO_LOCATION]
    for root,dirs,files in os.walk(globals.UPLOAD_FOLDER):
        collections.extend(dirs)
        break
    print("collections ", collections)
    return collections
  