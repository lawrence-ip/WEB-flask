#!/bin/python

import os
from pymongo import Mongoclient

mongo_host = 'localhost'
mongo_port = 27017

mongo_data_dir = 'mongo_data'

os.makedirs(mongo_data_dir,exis_ok=True)
mongo_data_path = os.path.join(os.getcwd(),mongo_data_dir)

