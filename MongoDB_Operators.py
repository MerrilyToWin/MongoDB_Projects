"""Finding Documents by Using Comparison Operators"""


"""$gt -- Use the $gt operator to match documents with a field greater than the given value. """

# For example:
# db.sales.find({ "items.price": { $gt: 50}})

"""$lt -- Use the $lt operator to match documents with a field less than the given value. """

# For example:
# db.sales.find({ "items.price": { $lt: 50}})

"""$lte -- Use the $lte operator to match documents with a field less than or equal to the given value. """

# For example:
# db.sales.find({ "customer.age": { $lte: 65}})

"""$gte -- Use the $gte operator to match documents with a field greater than or equal to the given value. """

# For example:
# db.sales.find({ "customer.age": { $gte: 65}})




"""Finding Documents by Using Logical Operators"""


"""$and -- Use implicit $and to select documents that match multiple expressions."""

# For example:
# db.routes.find({ "airline.name": "Southwest Airlines", stops: { $gte: 1 } })

"""$or -- Use the $or operator to select documents that match at least one of the included expressions. """

# For example:
# db.routes.find({
#   $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }],
# })


"""Use the $and operator to use multiple $or expressions in your query."""

# db.routes.find({
#   $and: [
#     { $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }] },
#     { $or: [{ "airline.name": "American Airlines" }, { airplane: 320 }] },
#   ]
# })


"""Incease and Decrease"""

# $inc -- Increases the number 
# example:
# {
#     update or filter : { "$inc": {"data":1}}
# }
