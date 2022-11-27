import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file_path = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__=="__main__" :
    df = pd.read_csv(data_file_path)
    print(f"Rows and columns: {df.shape}")

# Convert dataframe to json so that we can dump our all record in mongodb
    df.reset_index(drop=True,inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
#insert converted json record in to mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    



