from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key"  # 세션을 위한 비밀 키

# 더미 데이터 (실제로는 데이터베이스를 사용)
users = {
    "jieun@example.com": {
        "name": "김지은",
        "password": "password123",
        "level": "Silver"
    }
}

# 로그인 페이지
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = users.get(email)
        if user and user["password"] == password:
            session["user"] = {
                "name": user["name"],
                "email": email,
                "level": user["level"]
            }
            return redirect(url_for("user_page"))
        else:
            return render_template("login.html", error="이메일 또는 비밀번호가 잘못되었습니다.")
    return render_template("/html/login.html")

# 회원 페이지
@app.route("/user")
def user_page():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("user.html", user=session["user"])

# 로그아웃
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
