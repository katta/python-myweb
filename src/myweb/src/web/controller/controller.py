from flask import Blueprint

controller = Blueprint('controller', __name__)


@controller.route('/')
def hello():
    return 'Hello'
