from flask import Flask
from apis import api
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)