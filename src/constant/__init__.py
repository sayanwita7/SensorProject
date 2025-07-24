import os
from dotenv import load_dotenv
load_dotenv()

AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "SensorFaultDetection"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

TARGET_COLUMN="quality"

MODEL_FILE_NAME="model"
MODEL_FILE_EXTENSION=".pkl"

artifact_folder = "artifacts"