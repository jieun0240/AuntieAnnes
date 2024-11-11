from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# 홈 페이지 라우팅
@app.route('/')
def home():
    return render_template_string(base_html)

# 매장 검색 API 엔드포인트
@app.route('/search', methods=['POST'])
def search():
    search_query = request.json.get('query', '')
    # 예시 매장 데이터 (실제로는 API 연동 필요)
    results = [
        {"name": "앤티앤스 서울역사점", "address": "서울 용산구 동자동 43-205", "distance": "68m"}
    ]
    # 검색 결과 반환
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)