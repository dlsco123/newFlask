from flask import Blueprint
from flask import request
# db 적용을 위해
from pybo.models import Question, Answer
from datetime import datetime
from pybo import db

import time
import os

import torch
from torchvision import transforms
from PIL import Image

# 127.0.0.1:5000/classification/ -> 주소를 분기함
bp = Blueprint('classification', __name__, url_prefix='/classification') 
model = torch.load('model.pt', map_location=torch.device('cpu'))

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

@bp.route('/makale', methods=['POST'])
def makale():
    print(request.files)
    f = request.files['image']
    print(f)

    # 허용된 확장자 리스트
    allowed_extensions = ['.jpg', '.png', '.jpeg']

    # 파일 확장자 추출
    _, file_extension = os.path.splitext(f.filename)

    if file_extension.lower() not in allowed_extensions:
        return '사용할 수 없는 format 형식입니다.'
    else:
        # 파일 이름에 타임스탬프 추가하여 중복 방지 (소수점 제거)
        filename = os.path.splitext(f.filename)[0]
        unique_filename = f"{filename}_{int(time.time())}{file_extension}"
        f.save(unique_filename)
        image = Image.open(unique_filename)


    transform_test = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image = transform_test(image).unsqueeze(0).to('cpu')
    model.to('cpu')
    with torch.no_grad():
        outputs = model(image)
        print(outputs)
        _, preds = torch.max(outputs, 1)
        classname = ['마동석', '이국주', '카리나']
        print(classname[preds[0]])

    return classname[preds[0]] + '입니다.'


@bp.route('/get_question', methods=['GET', 'POST'])
def get_question():
    #TODO read
    # questions = Question.query.all()    #[question1, question2...]
    # print(len(questions))
    # result = Question.query.filter(Question.id == 1).all()
    # result = Question.query.filter(Question.content.like('%고%')).all()
    # print(result[0].subject)
    # print(result[0].content)

    #TODO update
    # result = Question.query.get(1)
    # result.subject = '제목을 바꿈1'
    # db.session.commit()

    #TODO delete
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()
    return '가져오기 성공'
