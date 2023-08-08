from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.models import Question
# blueprint : 주소 관리 역할

bp = Blueprint('main', __name__, url_prefix='/') 
# blueprint 객체 이름 = main
# url_prefix : '/'로 주소가 들어오는 경우 blueprint 처리 함

# 끝 주소가 '/'인 경우 아래 함수 실행
@bp.route('/')
def index():
    return redirect(url_for('question.q_list'))

@bp.route('/meta')
def mtvs():
    return '메타버스 아카데미 AI'

@bp.route('/ai')
def main_ai():
    return 'ai 최고'