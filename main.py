from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return{"data": "Hello World!!"}


api.add_resource(Hello, "/helloworld")

if __name__ == '__main__':
    # start server
    app.run(debug=True)
