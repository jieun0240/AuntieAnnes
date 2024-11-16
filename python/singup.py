# 회원가입 페이지 (추가 가능)
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
