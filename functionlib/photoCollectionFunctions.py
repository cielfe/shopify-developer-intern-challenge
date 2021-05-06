import os

from functionlib import globalVariables as globals
def isCollectionUnique(collection_name):
    '''This function returns a boolean value if a collection name is unique in the image repository
        Returns True if it is unique, False otherwise'''
    for root,dirs,files in os.walk(globals.UPLOAD_FOLDER):
        #only need to check the directory names
        if collection_name in dirs:
            return False
        break
    return True

def collectionExists(collection_name):
    '''This function returns a boolean value if a collection exists in the image repository
        Returns True if it is does, False otherwise'''
    for root,dirs,files in os.walk(globals.UPLOAD_FOLDER):
        #only need to check the directory names
        if collection_name in dirs:
            return True
        break
    return False
    
def photoExistsInCollection(file_name,collection_name):
    '''This function returns a boolean value if a specific photo name already exists in the collection
        Returns True if it does, False otherwise'''
    
    search_dir = ""
    if collection_name == globals.DEFAULT_PHOTO_LOCATION:
        search_dir = globals.UPLOAD_FOLDER 
    else:
         search_dir = globals.UPLOAD_FOLDER + "/"+collection_name
    print("===search_dir ", search_dir)
    for root,dirs,files in os.walk(search_dir):
        print("root is ", root)
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
  