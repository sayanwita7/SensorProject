import os
from dotenv import load_dotenv
load_dotenv()

MONGO_DATABASE_NAME = "SensorFaultDetection"
MONGO_COLLECTION_NAME = "waferfault"
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
TARGET_COLUMN = "quality"
MODEL_FILE_NAME="model"
MODEL_FILE_EXTENSION=".pkl"
artifact_folder = "artifacts"