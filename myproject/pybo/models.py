from pybo import db

class Question(db.Model): # 모든 모델의 기본 클래스인 db.Model을 상속받음. 이 때 db는 __init__.py 파일에서 생성한 SQLAlchemy 객체다
    id = db.Column(db.Integer, primary_key=True) # 고유번호
    subject = db.Column(db.String(200), nullable=False) # 제목
    content = db.Column(db.Text(), nullable=False) # 내용
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일시

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) # 질문 모델과 연결하려고 추가. 어떤 질문에 대한 압변인지 알아야 되므로. 
    #기존 모델과 연결된 속성을 foreign key. 'question.id'는 question table의 id column을 의미. # ondelete는 삭제 연동 설정
    question = db.relationship('Question', backref=db.backref('answer_set')) # 질문 모델을 참조하기 위해 추가
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)