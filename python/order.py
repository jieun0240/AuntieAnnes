from flask import Flask, jsonify, render_template

app = Flask(__name__)

# 샘플 메뉴 데이터 (데이터베이스나 외부 파일로 대체 가능)
menu_data = [
    {"name": "프레즐", "category": "프레즐", "img": "pretzel.jpg"},
    {"name": "스틱", "category": "스틱", "img": "stick.jpg"},
    {"name": "핫도그", "category": "핫도그", "img": "hotdog.jpg"},
    {"name": "딥", "category": "딥", "img": "dip.jpg"},
    {"name": "에이드", "category": "에이드", "img": "ade.jpg"},
    {"name": "커피", "category": "커피", "img": "coffee.jpg"}
]

# 메인 주문 페이지 (order.html) 라우트
@app.route('/')
def order():
    return render_template('html/order.html')

# 메뉴 데이터를 JSON 형태로 제공하는 라우트
@app.route('/static/js/menu.json')
def menu():
    return jsonify(menu_data)

if __name__ == '__main__':
    app.run(debug=True)
