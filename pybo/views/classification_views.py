from flask import Blueprint
from flask import request
# db 적용을 위해
from pybo.models import Question, Answer
from datetime import datetime
from pybo import db

# 127.0.0.1:5000/classification -> 이 이하의 주소를 분기함
bp = Blueprint('classification', __name__, url_prefix='/classification') 

@bp.route('/catdog')
def catdog():
    result = request.form
    print(result)
    print(result['chat']) # request.form dict에서 key가 chat인 것
    return 'cat'

@bp.route('/birdflower')
def birdflower():
    q = Question(subject='질문1', content='고양이 맞나요?', create_date = datetime.now()) # primary_key는 자동생성됨
    db.session.add(q) # db의 session에 추가
    db.session.commit() # session에 저장된 것이 실제(물리적으로) update됨
    return 'bird'

@bp.route('/makale')
def makale():
    # m = Question(subject='질문1', content='고양이 맞나요?', create_date = datetime.now()) # primary_key는 자동생성됨
    # db.session.add(m)
    # db.session.commit()
    return 'bird'
