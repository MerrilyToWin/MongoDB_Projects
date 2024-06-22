# Aggregation: Collection and summary of data
# Stage: One of the built-in methods that can be completed on the data, but does not permanently alter it
# Aggregation pipeline: A series of stages completed on the data in order


# Syntax
# db.collection.aggregate([
#     {
#         $match:{
#             {
#                 "expression":"find"
#             },
#         }
#     }
# ])



""" Types Of Aggreations"""
# Match - Matches all the data in the dataBase Collection ---> $match
# Group - Groups or combine all the dataBase in the collection ---> $group
# Sort -- Sorts the element in ascending or descending order --- $sort
# Limit -- Sets displaying limit --- $limit
# Project -- Its filters the necessary data that has to be displayed ex: like filter
# Set -- It sets the value in the data base ex: like update method
# Count -- Counts how many documents in the db
# Out -- Create new DataBase or Collection according to the syntax

"""$match syntax"""
# {
#   $match: {
#      "field_name": "value"
#   }
# }


"""$group syntax"""
# {
#   $group:
#     {
#       _id: <expression>, // Group key
#       <field>: { <accumulator> : <expression> }
#     }
# }


"""Example"""
# db.zips.aggregate([
# {   
#    $match: { 
#       state: "CA"
#     }
# },
# {
#    $group: {
#       _id: "$city",
#       totalZips: { $count : { } }
#    }
# }
# ])

"""$sort syntax"""
# {
#     $sort: {
#         "field_name": 1
#     }
# }

"""$limit syntax"""
# {
#   $limit: 5
# }


"""Example"""
# db.zips.aggregate([
# {
#   $sort: {
#     pop: -1
#   }
# },
# {
#   $limit:  5
# }
# ])

"""$project syntax"""
# {
#     $project: {
#         state:1, 
#         zip:1,
#         population:"$pop",
#         _id:0
#     }
# }

"""$set synatx"""
# {
#     $set: {
#         place: {
#             $concat:["$city",",","$state"]
#         },
#         pop:10000
#      }
#   }

"""$count syntax"""
# {
#   $count: "total_zips"
# }

"""$out syntax"""
# {
#     $out:"Collection_name"
# }