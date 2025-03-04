import requests
import pymongo
from pymongo import MongoClient

# MongoDB setup
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client["external_data"]
collection = db["posts"]

# Step 1: Fetch Data from External API
API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(API_URL)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

posts = response.json()

# Step 2: Extract Required Data
extracted_data = []
for post in posts:
    extracted_data.append({
        "post_id": post["id"],
        "title": post["title"],
        "body": post["body"],
        "user_id": post["userId"]
    })

# Step 3: Send Extracted Data to MongoDB
if extracted_data:
    collection.insert_many(extracted_data)
    print(f"Inserted {len(extracted_data)} posts into MongoDB.")
else:
    print("No data to insert.")

# Optional: Fetch and print to verify
print("Sample data from MongoDB:")
for doc in collection.find().limit(5):
    print(doc)

display all records from the table
SELECT * FROM Customers;

SELECT City FROM Customers

#Select all the different values from the table.
SELECT DISTINCT Country FROM Customers;

#Select all records where the column has the value specific.
SELECT * FROM Customers
WHERE City = 'Berlin';

#NOT keyword to select all records where condition is NOT.
SELECT * FROM Customers
WHERE NOT City = 'Berlin';

#Select all records where the column has the value specific.
SELECT * FROM Customers
WHERE Customer ID = 32;

#Select all records where columnd habe specifiec values.
SELECT * FROM Customers
 WHERE City = 'Berlin' AND PostalCode = 12209;

#Select all records where columns satisfy either one of the conditions.
SELECT * FROM Customers City = 'Berlin' OR City  = 'London';