from flask_restplus import Api

from user import user_api

api = Api(version='1.0', title='TodoMVC API',
    description='A simple API for Machine Learning')

api.add_namespace(user_api)
