from pybo import db

# 내 db에 question 이름을 가진 table 생성
# class : table, 안의 variable : column
# 어떤 db든 형식은 동일함
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False) # 글자 제한
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model): # 총4개의 columns
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))  # 질문에 대한 답변 번호
    # question.id 값은 foreignkey를 가짐 : (foreignkey) 다른 테이블의 primary key
    # CASCADE : 질문이 삭제된 경우 연결된 answer는 자동으로 삭제시킴
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False) # 글자 제한 없이 받음
    create_date = db.Column(db.DateTime(), nullable=False)
