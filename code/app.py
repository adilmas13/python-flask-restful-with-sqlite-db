from item import Item, ItemList
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate, identity
# Resource are concerned with entities eg Student. They are mapped with db
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'adil'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates /auth end point

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# run this only if it a main file ie it is executed via terminal
# will not run app if app is imported from another file
if __name__ == '__main__':
    app.run(port=5000, debug=True)
