from flask import Flask, request,jsonify,make_response,Blueprint
from flask_restful import Resource,Api
from pymongo import MongoClient
from newProject.project1 import insert,read,delete,updatee
from newProject import api, app
# from newProject import make_celery
# from newProject import celery
from newProject import create_access_token,JWTManager,get_jwt_identity,jwt_required

example = Blueprint("api",__name__)

client = MongoClient()
mydatebase = client.User

mycollection = mydatebase.Users


# print(mycollection)

'''
response type 
exception handling
difference betweeen find and fine_one query -> and its outputs.
diff betwewen match {matchhh},{} in mongo and "$eq"???
'''
# @app.route("/",method=[get,post])
class UserRegeister(Resource):
    def post(self):
        try:
            username = request.json.get("username", "NA")
            password = request.json.get("password", "NA")
            age = request.json.get("age", 0)
            val = {"username": username, "password": password, "age": age}
            if username =="NA" or username=="" or password =="NA" or password==""  or age=="NA":
                return jsonify({"message":"Username or Password or age is wrong"})
            else:
                insert1 = insert(val)
                # a = username
                # reverse.delay(a)
                return jsonify({"message":"Succefully register!"})


        except Exception as e:
            return jsonify({"error": str(e)})


# @celery.task(name='reverse')
# def reverse(name):
#     return name[::-1]




class Read(Resource):
    def post(self):
        #cursor = mycollection.find()
        username = request.json.get("username")
        password = request.json.get("password")
        #db.Users.find({username: "Amit"}, password: "password"})
        findquery = {"username": username, "password": password}
        projection = {"username": 1,"age":1, "_id": 0}
        cursor = read(findquery,projection)
        n = cursor
        try:
            if n:
                user = n.get('username')

                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token)
                return jsonify({"message": f"User {user} is Present "})
            else:
                return jsonify({"message": f"User {username} is not Present"})
        except Exception as e:
            return jsonify({"error": str(e)})

class Delete(Resource):
    @jwt_required()
    def post(self):
        username= request.json.get("username")
        fin = {"username":username}
        query = delete(fin)
        count1 = query
        try:
            if count1 == 0:
                return jsonify({"message": "No Such user exists"})
            else:
                current_user = get_jwt_identity()
                return jsonify({"message": "User deleted sucessfully!"})
        except Exception as e:
            return jsonify({"error": str(e)})

class Update(Resource):
    #@jwt_required()
    def post(self):
         try:
             username =request.json.get("username","NA")
             age = request.json.get("age","NA")

             find = {"username":username}
             update = {"$set":{"age":age}}
             query = updatee(find,update)
             print(query)
             ack = query[0]
             match = query[1]
             # print("This is match",match)
             if ack == True and match>0:
                 return jsonify({"message": f"Age updated to {age}"})
             else:
                 return jsonify({"message": "Error in updating Check username Exist!"})
         except Exception as e:
             import traceback
             print(traceback.print_exc())
             return jsonify({"error": str(e)})


api.add_resource(UserRegeister,'/insert')
api.add_resource(Read,"/read")
api.add_resource(Delete,"/delete")
api.add_resource(Update,"/update")

# o.add_resource(UserRegeister,'/insert')
# o.add_resource(Read,"/read")
# o.add_resource(Delete,"/delete")
# o.add_resource(Update,"/update")


