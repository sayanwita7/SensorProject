from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import os
from dotenv import load_dotenv
load_dotenv()
uri=os.getenv("MONGO_DB_URL")
client=MongoClient(uri)
DATABASE_NAME="SensorFaultDetection"
COLLECTION_NAME='waferfault'
df=pd.read_csv(r"C:\Users\deysa\SensorProject\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)