from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from flask_cors import CORS

app = Flask('db')
api = Api(app)
CORS(app)



class Rest(Resource):
    users = []


    def save(self):
        with open('db.json','w') as file:
            file.write(json.dumps(self.users))

    def load(self):
        with open('db.json','r') as file:
            self.users = json.loads(file.read())

    def post(self):
        self.load()
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='args')
        parser.add_argument('password', type=str, location='args')
        name = parser.parse_args().name
        password = parser.parse_args().password

        exists = any(student['name'] == name for student in self.users)

        if exists:
            return "users already exists"
        else:

            self.users+=[
                {
                    'name': name,
                    'password' : password
                }
            ]
            self.save()
            return "users has been created"


    def get(self):
        self.load()
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str,location='args')
        parser.add_argument('password',type=str, location='args')

        name = parser.parse_args().name
        password = parser.parse_args().password


        for user in self.users:
            if user['name'] == name and user['password'] == password:
                return user
        return self.users

    def put(self):
        self.load()
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str,location='args')
        parser.add_argument('password',type=str, location='args')

        name = parser.parse_args().name
        password = parser.parse_args().password

        for user in self.users:
            if user['name'] == name:
                if password != None:
                    user['password'] = password
                    self.save()
                    return "password has been updated"
                else:
                    return "password must not be empty"
            else:
                return "incorrect username"

    def delete(self):
        self.load()
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str, location='args')
        parser.add_argument('password',type=str, location='args')

        name = parser.parse_args().name
        password = parser.parse_args().password

        for user in self.users:
            if user['name'] == name and  user['password'] == password:
                self.users.remove(user)
                self.save()
                return "user has been deleted"

        return "wrong username or password"



api.add_resource(Rest, '/login')
if __name__ == '__main__':
    app.run(debug=True)