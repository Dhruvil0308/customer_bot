from pymongo import MongoClient
client=MongoClient("mongodb+srv://dhruvil08:S0RPLc64iyyZELNm@cluster0.n7hmy.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database("customer_bot")
try:
    client.admin.command("ping")
    print("Connected")
except Exception as e:
    print(e)

def get_db():
    return db