from flask import Flask
from views import router

app = Flask(__name__)
app.secret_key = "secret key"
app.register_blueprint(router)