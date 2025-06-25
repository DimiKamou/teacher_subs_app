from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return 'Teacher Substitution System is running!'
