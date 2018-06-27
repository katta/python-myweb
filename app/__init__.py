from flask import Flask
from app.controller import controller

app = Flask(__name__)
app.register_blueprint(controller)
