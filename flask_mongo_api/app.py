from flask import Flask, jsonify
from dotenv import load_dotenv
import pymongo
import os

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

# Database and Collection
db = client["flask_db"]
collection = db["students"]

app = Flask(__name__)

# Insert sample data if collection empty
if collection.count_documents({}) == 0:
    sample_data = [
        {"name": "Himanshu", "age": 21},
        {"name": "Rahul", "age": 22},
        {"name": "Aman", "age": 20}
    ]
    collection.insert_many(sample_data)


# API Route
@app.route("/api")
def api():
    
    data = list(collection.find({}, {"_id": 0}))   # remove _id

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)