from pymongo import MongoClient


# Database connection
CONNECTION_STRING = "mongodb://localhost:27017/"
client = MongoClient(CONNECTION_STRING)
# Create database
db_name = client['books_db']
# create col name
col_name = db_name['kitap_sepeti']
