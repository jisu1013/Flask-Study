from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/') # 이름, 모듈명, URL prefix

@bp.route('/hello') #URL에서 /에 mapping되는 함수이다. 그 mapping을 애너테이션이 만들어준다
# 애너테이션으로 매핑되는 함수를 라우트 함수라고 한다
def hello_pybo():
    return 'Hello, Pybo!' # Hello Pybo!를 출력

@bp.route('/')
def index():
    return redirect(url_for('question._list'))