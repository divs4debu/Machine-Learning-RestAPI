from flask_restplus import Namespace, Resource, fields
from flask import request

user_api = Namespace('user', description='User related operations', path='/')

user = user_api.model('User', {
    'id': fields.Integer(readOnly=True, description='Auto incremented value for unique purposes'),
    'email': fields.String(required=True)
})


class UserDAO(object):

    def __init__(self):
        self.id = 0
        self.email = ""
        self.users = list()

    def create(self, data):
        user = data
        user['id'] = self.id = self.id+1
        self.users.append(user)
        return user

    def get(self, id):
        for u in self.users:
            if u['id'] == id:
                return u

    def getAll(self):
        return self.users

    def update(self, id, data):
        user = self.get(id)
        user.update(data)
        return user

    def delete(self, id):
        user = self.get(id)
        self.users.remove(user)

IMemDAO = UserDAO()


@user_api.route('/users')
class UserBulkOperations(Resource):

    @user_api.marshal_list_with(user)
    def get(self):
        print (IMemDAO.users)
        return IMemDAO.users

    @user_api.expect(user)
    @user_api.marshal_with(user)
    def post(self):
        json = request.get_json()
        return IMemDAO.create(json), 201


@user_api.route('/user/<int:id>')
class UserOperations(Resource):

    @user_api.param('id', 'User identifier')
    def get(self, id):
        return IMemDAO.get(id)

    @user_api.expect(user)
    @user_api.marshal_with(user)
    def put(self, id):
        json = request.get_json()
        return IMemDAO.update(id, json)

    def delete(self, id):
        return IMemDAO.delete(id)
