from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(): # 어플리케이션 팩토리, 다른 이름을 사용하면 정상적으로 동작하지 않는데, 그 이유는 플라스크 내부에서 정의된 함수명이기 때문.
    app = Flask(__name__)
    app.config.from_object(config) # config.py 파일에 작성된 항목을 app.config 환경변수로 부름

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루 프린트
    from .views import main_views, question_views, answer_views # create_app 함수에 등록된 hello_pybo 함수 대신 blueprint를 사용하도록 변경
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app