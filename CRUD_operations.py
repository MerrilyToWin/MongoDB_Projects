from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from bson import ObjectId
import ast



print("___________________________WELCOME TO PROJECT M___________________________\n")
print("Connecting to server..............")

user = 'user name'
password = 'user password'

uri = f"mongodb+srv://{user}:{password}@projectcluster.ccidztr.mongodb.net/?retryWrites=true&w=majority&appName=ProjectCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Did not connect to the server, Try this methods:\n1) Check your user name and password\n2 Change the IP address in Network access")




myDB = client["Project_M"]
myCollection = myDB["Collection"]
mycol = myDB["one_col"]


one_col = [
        {
            "firstName": "Sophia",
            "lastName": "H",
            "age": 22,
            "gender": "Female",
            "address": {"city": "Hyderabad", "state": "Telangana", "country": "India"},
            "countryCode": "+91",
            "phoneNumber": 8442567932,
            "skills": [
                {"name": "JAVASCRIPT", "level": 8},
                {"name": "PYTHON", "level": 7},
                {"name": "C", "level": 5},
            ],
            "createdAt": datetime.datetime.now(),
        },
]


Collection = [
        {
            "firstName": "Aarav",
            "lastName": "K",
            "age": 25,
            "gender": "Male",
            "address": {"city": "Bangalore", "state": "Karnataka", "country": "India"},
            "countryCode": "+91",
            "phoneNumber": 9876543210,
            "skills": [
                {"name": "JAVA", "level": 9},
                {"name": "PYTHON", "level": 6},
                {"name": "SQL", "level": 7},
            ],
            "createdAt": datetime.datetime.now(),
        },
        {
            "firstName": "Maya",
            "lastName": "S",
            "age": 30,
            "gender": "Female",
            "address": {"city": "Mumbai", "state": "Maharashtra", "country": "India"},
            "countryCode": "+91",
            "phoneNumber": 9123456789,
            "skills": [
                {"name": "HTML", "level": 8},
                {"name": "CSS", "level": 7},
                {"name": "JAVASCRIPT", "level": 7},
            ],
            "createdAt": datetime.datetime.now(),
        }
    ]

def create_one(one_col):
    mycol.insert_one(one_col)

def create_many(Collection):
    myCollection.insert_many(Collection)

def read_one(filters,query):
    data = myCollection.find(query,filters)
    
def read(filters,query):
    data = myCollection.find(query,filters)
    filt = list(filters)
    for i in data:
        print(i[filt[0]])

def up_one(filters,query):
    myCollection.update_one(query,filters)

def up_many(filters,query):
    myCollection.update_many(query,filters)

def dele(query):
    myCollection.delete_one(query)

def dele_many():
    myCollection.delete_many({})

def dropAll():
    myCollection.drop()

    


num = int(input("\n1. Create\n2. Create Many\n3. Read One\n4. Read All\n5. Update One\n6. Upadte All\n7. Delete One\n8. Delete All\n9. Drop\nEnter your operation: "))

def query():
    d={}
    loops = int(input("Enter how many query you want to add: "))
    for i in range(loops):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        if value > "0" and value <= "99999999999":
            value = int(value)
        d.update({key:value})
    return d

def filters():
    d={}
    loops = int(input("Enter how many filter you want to add: "))
    for i in range(loops):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        if value > "0" and value <= "9":
            value = int(value)
        if num == 6 or num == 5:
            value = ast.literal_eval(value)
        d.update({key:value})
    print("\n")
    return d


if num == 1:
    create_one(one_col)
    print("----------------Your data Has been uploaded successfully----------------")

elif num == 2:
    create_many(Collection)
    print("----------------Your data Has been uploaded successfully----------------")

elif num == 3:
    print("_______________________Your Data_______________________")
    read_one(filters(),query())

elif num == 4:
    print("_______________________Your Data_______________________")
    read(filters(),query())

elif num == 5:
    up_one(filters(),query())
    print("----------------Your Data is being updated!!----------------")

elif num == 6:
    up_many(filters(),query())
    print("----------------Your Data is being updated!!----------------")

elif num == 7:
    dele(query())
    print("----------------Your Data is being Deleted!!----------------")

elif num == 8:
    dele_many()
    print("----------------Your Data is being Deleted!!----------------")

elif num == 9:
    dropAll()
    print("----------------Your Collection has been deleted----------------")

else:
    print("Wrong input")




