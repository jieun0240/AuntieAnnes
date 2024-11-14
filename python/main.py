from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 예시 메뉴 데이터 (카테고리별로 데이터를 준비)
menu_data = [
    {"id": 1, "name": "프레즐 1", "category": "프레즐", "img": "스크롤이미지-1.jpg"},
    {"id": 2, "name": "프레즐 2", "category": "프레즐", "img": "스크롤이미지-2.jpg"},
    {"id": 3, "name": "스틱 1", "category": "스틱", "img": "스크롤이미지-3.jpg"},
    {"id": 4, "name": "핫도그 1", "category": "핫도그", "img": "스크롤이미지-1.jpg"},
    {"id": 5, "name": "에이드 1", "category": "에이드", "img": "스크롤이미지-2.jpg"},
    {"id": 6, "name": "커피 1", "category": "커피", "img": "스크롤이미지-3.jpg"}
]

# 메인 페이지 라우트
@app.route('/')
def index():
    return render_template('/html/main.html')  # HTML 템플릿 렌더링

# 메뉴 데이터를 JSON 형식으로 반환하는 라우트
@app.route('/menu')
def get_menu():
    return jsonify(menu_data)

# 특정 카테고리로 필터링된 메뉴 데이터를 JSON으로 반환하는 라우트
@app.route('/menu/<category>')
def get_menu_by_category(category):
    filtered_menu = [item for item in menu_data if item['category'] == category]
    return jsonify(filtered_menu)

if __name__ == '__main__':
    app.run(debug=True)
