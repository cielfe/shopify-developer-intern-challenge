from .photo_api import PhotosApi,PhotoApi
from .collection_api import CollectionsApi
def initialize_routes(api):
    ####APIs for web-app functionalities - START
    api.add_resource(PhotosApi, "/api/photo")
    api.add_resource(PhotoApi, "/api/photo/<name>")

    api.add_resource(CollectionsApi,"/api/collection")