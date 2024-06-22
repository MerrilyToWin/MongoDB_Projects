from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from bson import ObjectId


user = 'merwin'
password = 'AmmaMerwin'

uri = f"mongodb+srv://{user}:{password}@project.dkgp55t.mongodb.net/?retryWrites=true&w=majority&appName=Project"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""Create a Database"""

class_a = client["Class_Details"]

"""Create a collection"""

students = class_a["student"]

"""Data To be inserted"""

student = [
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
    },
    {
        "firstName": "Rohan",
        "lastName": "M",
        "age": 28,
        "gender": "Male",
        "address": {"city": "Delhi", "state": "Delhi", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9988776655,
        "skills": [
            {"name": "C++", "level": 8},
            {"name": "JAVA", "level": 7},
            {"name": "PYTHON", "level": 6},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Priya",
        "lastName": "N",
        "age": 26,
        "gender": "Female",
        "address": {"city": "Chennai", "state": "Tamil Nadu", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9876541234,
        "skills": [
            {"name": "C#", "level": 7},
            {"name": "ASP.NET", "level": 8},
            {"name": "SQL", "level": 6},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Arjun",
        "lastName": "R",
        "age": 29,
        "gender": "Male",
        "address": {"city": "Pune", "state": "Maharashtra", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 8765432109,
        "skills": [
            {"name": "PYTHON", "level": 9},
            {"name": "R", "level": 7},
            {"name": "SQL", "level": 7},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Kavya",
        "lastName": "T",
        "age": 24,
        "gender": "Female",
        "address": {"city": "Kolkata", "state": "West Bengal", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9234567890,
        "skills": [
            {"name": "RUBY", "level": 8},
            {"name": "RAILS", "level": 7},
            {"name": "JAVASCRIPT", "level": 6},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Vikram",
        "lastName": "D",
        "age": 31,
        "gender": "Male",
        "address": {"city": "Ahmedabad", "state": "Gujarat", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9123450987,
        "skills": [
            {"name": "PHP", "level": 7},
            {"name": "LARAVEL", "level": 8},
            {"name": "SQL", "level": 7},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Neha",
        "lastName": "V",
        "age": 27,
        "gender": "Female",
        "address": {"city": "Jaipur", "state": "Rajasthan", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9988001122,
        "skills": [
            {"name": "SWIFT", "level": 7},
            {"name": "OBJECTIVE-C", "level": 6},
            {"name": "JAVASCRIPT", "level": 5},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Ishaan",
        "lastName": "P",
        "age": 23,
        "gender": "Male",
        "address": {"city": "Gurgaon", "state": "Haryana", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9876540987,
        "skills": [
            {"name": "NODE.JS", "level": 8},
            {"name": "EXPRESS", "level": 7},
            {"name": "MONGODB", "level": 6},
        ],
        "createdAt": datetime.datetime.now(),
    },
    {
        "firstName": "Ananya",
        "lastName": "J",
        "age": 22,
        "gender": "Female",
        "address": {"city": "Lucknow", "state": "Uttar Pradesh", "country": "India"},
        "countryCode": "+91",
        "phoneNumber": 9087654321,
        "skills": [
            {"name": "JAVA", "level": 8},
            {"name": "SPRING", "level": 7},
            {"name": "HIBERNATE", "level": 6},
        ],
        "createdAt": datetime.datetime.now(),
    }
]


# """Function Insert_one - Inserts only one document"""
# """Syntax - Collection_name . function_name (data)"""

# students.insert_one(student)

# """Function Insert_many - Inserts all the data from the dictonary"""

# students.insert_many(student)


# """Function Find_one - Reads only one document"""

# query = {"firstName": "Ananya"}

# filter = {"skills": 1}

# print(students.find_one(query,filter))

# """Function Find - Reads all the Data"""


# """Query"""

# query = {
#     "countryCode": "+91",
#     }

# myquery = { "address": { "$gt": "S" } } """-- Address Starting with S and greater than S - "$gt"""
# myquery = { "address": { "$regex": "^S" } } """ ----- Address Starting with only S - "$regex"""

# """Filter """

# filters = {
#     "firstName":1,
#     "_id":0
# }

# data = students.find(query,filters)


# for i in data:
#     print(i["firstName"])


# """Function Sort - Sorts The Values in Ascending or Desending Order"""

# data = students.find(query,filters).sort("firstName") """--- Ascending Order"""

# data = students.find(query,filters).sort("firstName") """--- Descending Order"""

# for i in data:
#     print(i)


# """Function Limit - Shows how many Documents are needed to view to maximum"""

# data = students.find(query,filters).limit(5) """---- Shows only 5 elements in the collection"""

# data = students.find(query,filters).limit(5).sort("firstName")

# for i in data:
#     print(i)

# """Function Update_one - Updates data in the collection of the selected data"""

# query = {"_id": ObjectId("666afe13d37672886d33bc0c")}

# updateData = {"$set": {"age": 22}}

# students.update_one(query, updateData)


# """Function Update_many - Updates data across the collection"""

# query = {"age": 22}

# updateData = {"$set": {"age": 20}}

# students.update_many(query, updateData)


# """Function Delete_one - Deletes specific data in the collection"""

# query = {"_id": ObjectId("666aff7c4603a596df92c37b")}
# students.delete_one(query)

# """Function Delete_many - Deletes all the data in the collection"""

# students.delete_many({})

# """Function Drop - Deletes the Collection"""

# students.drop()

# """Function countDocuments - Counts all the documents in the collection"""

# students.count_documents({}) -- """To Get all the document count"""
# students.count_documents({ "firstName": { "$gt": "S" }})



"""_________________________________Aggregation_________________________________"""

# result = students.aggregate(
#     [
#         {   
#             "$match": { 
#                 "age": 26
#                 }
#         },
#         {
#             "$group": 
#             {
#                 "_id": "$firstName",
#                 "totalZips": { "$count" : { } }
#             }
#         },
#         {
#             "$out":"Small_Details"
#         }
#     ]
# )


# result = students.aggregate([
#     {
#         "$sort":{
#             "age":1
#         }
#     },
#     {
#         "$limit":5
#     }
# ])


# result = students.aggregate([
#     {
#         "$project":{
#             "firstName":1,
#             "lastName":0,
#             "middleName":"Marie",
#         }
#     },
#     {
#         "$set": {
#             "age": 20
#             }
#         },
#     {
#         "$count":"firstName"
#     }
# ])

# print(result)

"""_________________________________Indexes_________________________________"""


"""Single Index"""

# result = students.create_index({
#   "firstName": 1
# })

# res=students.explain().find(
#     {
#         "firstName":"Neha"
#     }
# )


"""Compound Indexes"""

# students.createIndex({
#   "firstName":1, 
#   "lastName":-1,
# })


"""Deleting an index"""

# students.dropIndex(
#   'active_1_birthdate_-1_name_1'
# )

# students.dropIndex({
#   "active":1,
#   "birthdate":-1, 
#   "name":1
# })