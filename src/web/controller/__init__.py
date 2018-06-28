from flask import Flask
from controller import controller

app = Flask(__name__)
app.register_blueprint(controller)
