from collections import UserDict, UserList
from os import lseek
from flask import Flask, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from flask import jsonify, request




app = Flask(__name__)
app.secret_key="secretkey"

app.config['MONGO_URI']="mongodb://localhost/pythonreactdb"
mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])

def createUser():
   id = db.insert({
     
       'name':request.json['name'],
       'email':request.json['email'],
       'password':request.json['password']
   })

   return jsonify(str(ObjectId(id)))
   return 'received'

@app.route('/users', methods=['GET'])
def getUser():
    return'received'

@app.route('/users', methods=['GET'])
def deleteUser():
    return'received'

@app.route('/users', methods=['PUT'])
def updateUser():
    return'received'

if __name__ == "__main__":
    app.run(port=3000, debug=True)
