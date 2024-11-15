from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 라우트 설정
@app.route('/')
def login():
    return render_template('/html/login.html')  # 로그인 페이지 렌더링

@app.route('/signup')
def signup():
    return render_template('signup.html')  # 회원가입 페이지 렌더링

@app.route('/main', methods=['POST'])
def main():
    # 사용자가 제출한 로그인 데이터를 처리
    email = request.form.get('email')
    password = request.form.get('password')

    # 간단한 로그인 검증 (실제 검증은 데이터베이스에서 수행)
    if email == 'admin@example.com' and password == '1234':
        return render_template('main.html')  # 성공 시 메인 페이지 렌더링
    else:
        return '<h1>로그인 실패. 이메일과 비밀번호를 확인하세요!</h1>'  # 실패 시 메시지 표시

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)