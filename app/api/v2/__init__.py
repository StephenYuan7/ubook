from flask import Blueprint


def create_blueprint_v2():
    bp_v2 = Blueprint('v2', __name__)
    return bp_v2
