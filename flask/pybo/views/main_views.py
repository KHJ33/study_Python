from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/hhh')
def hello_pybo2():
    return '현정이를 사랑해'