from flask import Blueprint
from app.api.v2 import client


def create_blueprint_v2():
    bp_v2 = Blueprint('v2', __name__)
    client.api.register(bp_v2)
    return bp_v2
