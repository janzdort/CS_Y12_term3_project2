from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

PORT = 21370

app = Flask(__name__)
api = Api(app)


class MyResource(Resource):

    def post(self):
        print(request.values)
        if request.is_json:
            data = request.get_json()
            print|(data)
            return data, 200
        else:
            abort(422)

api.add_resource(MyResource, '/id')

if __name__ == '__main__':
    app.run(port=PORT)


