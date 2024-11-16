from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# 비밀 키 설정 (세션과 플래시 메시지에 사용)
app.secret_key = 'your_secret_key'

# SQLite 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auntieannes.db'  # 데이터베이스 파일 경로
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Flask-SQLAlchemy의 기본 알림을 끄기

# 데이터베이스 객체 생성
db = SQLAlchemy(app)

# User 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 사용자 ID (자동 증가)
    email = db.Column(db.String(150), unique=True, nullable=False)  # 이메일 (중복 불가)
    password = db.Column(db.String(200), nullable=False)  # 암호화된 비밀번호

# DB 초기화 (데이터베이스 파일 생성)
with app.app_context():
    db.create_all()

# 회원가입 페이지
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')  # 비밀번호 암호화

        # 이메일 중복 확인
        if User.query.filter_by(email=email).first():
            flash('이미 존재하는 이메일입니다.', 'error')
            return redirect(url_for('signup'))

        # 새로운 사용자 생성
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)  # DB에 새 사용자 추가
        db.session.commit()  # DB에 저장
        flash('회원가입 성공! 로그인하세요.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')  # GET 요청 시 회원가입 폼 렌더링

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()  # 이메일로 사용자 조회
        if user and check_password_hash(user.password, password):  # 비밀번호 확인
            flash('로그인 성공!', 'success')
            return redirect(url_for('main'))  # 로그인 성공 시 메인 페이지로 이동
        else:
            flash('이메일 또는 비밀번호가 잘못되었습니다.', 'error')
            return render_template('html/login.html')  # 로그인 실패 시 다시 로그인 페이지

    return render_template('html/login.html')  # GET 요청 시 로그인 폼 렌더링

# 메인 페이지 (로그인 후 이동)
@app.route('/main')
def main():
    return "안녕하세요! 로그인에 성공했습니다."

if __name__ == '__main__':
    app.run(debug=True)
