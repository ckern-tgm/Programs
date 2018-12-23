from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import json

app = Flask('db')
api = Api(app)
CORS(app)

class Rest(Resource):
    users = []

    def save(self):
        with open('db.json', 'w') as file:
            file.write(json.dumps(self.users))


    def load(self):
        with open('db.json','r') as file:
            self.users = json.loads(file.read())

    def post(self):
        self.load()
        parser = reqparse.RequestParser()
        parser.add_argument('vname', type=str, location='args')
        parser.add_argument('nname', type=str, location='args')

        vname = parser.parse_args().vname
        nname = parser.parse_args().nname

        exists = any(u['vname'] == vname for u in self.users)
        for u in self.users:
            if exists:
                return "User already exists"

        self.users+=[
            {
                "vname" : vname,
                "nname" : nname
            }
        ]
        self.save()
        return "User added"

    def get(self):
        self.load()

        parser = reqparse.RequestParser()
        parser.add_argument('vname', type=str, location='args')
        vname = parser.parse_args().vname

        for usr in self.users:
            if usr['vname'] == vname:
                return usr
        return self.users




api.add_resource(Rest, '/')
if __name__ == '__main__':
    app.run(debug=True)
