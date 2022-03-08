from flask import Flask
import flask_restful as restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'GUNDAM'}

api.add_resource(HelloWorld, '/')

class Trends(restful.Resource):
    def get(self):
        # put application's code here
        return {'2016': '2000', "2017": "3000"}

api.add_resource(Trends, "/Trends")

if __name__ == '__main__':
    app.run(debug=True)