from flask import Flask, render_template, request, redirect, url_for, flash, session
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

# 메인 라우트 (로그인 페이지로 리다이렉트)
@app.route('/')
def index():
    return redirect(url_for('login'))

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()  # 이메일로 사용자 조회
        if user and check_password_hash(user.password, password):  # 비밀번호 확인
            session['user_id'] = user.id  # 세션에 사용자 ID 저장
            session['user_email'] = user.email  # 세션에 사용자 이메일 저장
            flash('로그인 성공!', 'success')
            return redirect(url_for('main'))  # 로그인 성공 시 메인 페이지로 이동
        else:
            flash('이메일 또는 비밀번호가 잘못되었습니다.', 'error')
            return render_template('html/login.html')  # 로그인 실패 시 다시 로그인 페이지

    return render_template('html/login.html')  # GET 요청 시 로그인 폼 렌더링

# 회원가입 페이지
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  # 비밀번호 암호화

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

    return render_template('html/signup.html')  # GET 요청 시 회원가입 폼 렌더링

# 메인 페이지 (로그인 후 이동)
@app.route('/main')
def main():
    return render_template('html/main.html', message="안녕하세요! 로그인에 성공했습니다.")

# 사용자 페이지
@app.route('/user')
def user():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user_data = {
                'name': user.email.split('@')[0],  # 이메일의 @ 앞부분을 이름으로 사용
                'email': user.email,
                'level': '일반 회원'  # 예시, 실제 등급 시스템에 따라 수정 필요
            }
            return render_template('html/user.html', user=user_data)
    return redirect(url_for('login'))

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('login'))

# 기타 필요한 라우트들 (예: 장바구니, 주문 등)
@app.route('/cart')
def cart():
    return render_template('html/cart.html')

@app.route('/list')
def list():
    return render_template('html/list.html')    

@app.route('/order')
def order():
    return render_template('html/order.html')

@app.route('/store-selection')
def store_selection():
    return render_template('html/storeSelection.html')

if __name__ == '__main__':
    app.run(debug=True)