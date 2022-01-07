from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question') # 이름, 모듈명, URL prefix

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc()) # 질문 목록 데이터를 얻을 수 있음
    return render_template('question/question_list.html', question_list=question_list) # question/question_list.html 파일을 템플릿 파일이라고 함

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)