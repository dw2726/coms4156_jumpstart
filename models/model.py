from google.cloud import datastore
from flask import current_app

class Model:

    def get_client(self): 
        return datastore.Client('high-service-168907')

