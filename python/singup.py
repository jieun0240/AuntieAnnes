from flask import Flask, request, flash, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # session 및 flash 메시지를 위해 secret key가 필요합니다.

# DB 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# 모델 정의 (User 모델 예시)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # 비밀번호 확인
        if password != confirm_password:
            flash('비밀번호가 일치하지 않습니다.', 'error')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password, method='sha256')

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

if __name__ == '__main__':
    app.run(debug=True)
