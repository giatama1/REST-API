from flask import Flask, request
from flask_restful import Resource, Api
from resources.dataUser import dataUser_api

import models


app = Flask(__name__)
app.register_blueprint(dataUser_api)

#api = Api(app)
#api.add_resource(message.DataUserList, '/data_user', endpoint='data_user')

if __name__ == "__main__":
    models.initialize()
    app.run(debug=True)
