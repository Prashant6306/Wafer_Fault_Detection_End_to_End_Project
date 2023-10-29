from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pandas as pd
uri = "mongodb+srv://prashantsparhad:QcljYs1m6pIQthQ0@cluster0.bqnrlf4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

# read the data as a dataframe
df=pd.read_csv(r"C:\Users\ADMIN\Desktop\ML_Project\Wafer Fault Detection\Own_Sensor_Fault\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# from pymongo.mongo_client import MongoClient
# import pandas as pd
# import json

# # uniform resource indentifier
# uri = "mongodb+srv://snshrivas:Snshrivas@cluster0.u46c4.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # create database name and collection name
# DATABASE_NAME="pwskills"
# COLLECTION_NAME="waferfault"

# # read the data as a dataframe
# df=pd.read_csv(r"C:\Study1\ALL_PROJECTS\wafer_fault_detection_pw\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")
# df=df.drop("Unnamed: 0",axis=1)

# # Convert the data into json
# json_record=list(json.loads(df.T.to_json()).values())

# #now dump the data into the database
# client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
