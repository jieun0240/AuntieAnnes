from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션과 플래시 메시지를 위해 필요
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auntieannes.db'  # SQLite DB 설정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# DB 초기화
with app.app_context():
    db.create_all()

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('로그인 성공!', 'success')
            return redirect(url_for('main'))  # 메인 페이지로 이동
        else:
            flash('이메일 또는 비밀번호가 잘못되었습니다.', 'error')
            return render_template('login.html', error='이메일 또는 비밀번호가 잘못되었습니다.')

    return render_template('login.html')

# 회원가입 페이지 (추가 가능)
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

        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입 성공! 로그인하세요.', 'success')
        return redirect(url_for('login'))

    return render_template('html/signup.html')

# 메인 페이지 (샘플)
@app.route('/main')
def main():
    return "안녕하세요! 로그인에 성공했습니다."

if __name__ == '__main__':
    app.run(debug=True)
