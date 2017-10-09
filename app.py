from flask import Flask
from apis import api
import db

app = Flask(__name__)

api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)