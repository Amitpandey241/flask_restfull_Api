from pymongo import MongoClient

client = MongoClient()
mydatebase = client.User
mycollection = mydatebase.Users


#insert query
def insert(a):
    query = mycollection.insert_one(a)


#read query
def read(a,b, **kwargs):
    # findquery = {"username": username, "password": password}
    # projection = {"username": 1, "age": 1, "_id": 0}
    try:
        cursor = mycollection.find_one(a, b)
        return cursor
    except Exception as e:
        return {str(e)}

#delete query
def delete(find):
    try:
        query = mycollection.delete_one(find)
        return query.deleted_count
    except Exception as e:
        return {str(e)}

# n = {"username":"Controller"}
# # insert(n)
# res =delete(n)
# print(res)

#update query

def updatee(find,update):
    #a represents match{}
    #b represents projection
    # find = {"username": username}
    # update = {"$set": {"age": age}}
    try:
        query = mycollection.update_one(find, update)
        ack = query.acknowledged
        match = query.modified_count
        return [ack, match]
    except Exception as e:
        return {str(e)}

# n = {"username":"Amit"}
# #insert(n)
# up = {"$set":{"age":24}}
# u = update(n,up)
# print(u)
