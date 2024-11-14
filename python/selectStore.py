from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 홈 페이지 (네비게이션과 함께 기본 레이아웃 제공)
@app.route('/')
def home():
    return render_template('map.html')

# 매장 검색 API 엔드포인트 (추후 Naver API 등과 연동 가능)
@app.route('/search', methods=['POST'])
def search():
    search_query = request.json.get('query', '')
    # TODO: 검색어를 이용해 지도 API로 매장 데이터를 가져오는 코드 작성
    # 예시 데이터 반환 (실제 구현 시 지도 API 연동)
    results = [
        {"name": "앤티앤스 서울역사점", "address": "서울 용산구 동자동 43-205", "distance": "68m", "phone": "010-9023-9912"}
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
