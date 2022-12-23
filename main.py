from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api()

text = {

}


def post(text_id):
    parser = reqparse.RequestParser()
    parser.add_argument("text", type=str)
    text[text_id] = parser.parse_args()
    return text


class Main(Resource):
    pass


api.add_resource(Main, "/api")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
