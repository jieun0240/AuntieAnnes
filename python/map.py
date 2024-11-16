from flask import Flask, render_template, jsonify

app = Flask(__name__)

# JSON 데이터
regions = {
    "서울특별시": [
        {"district": "강남구", "stores": ["강남역점", "신사점", "압구정점"]},
        {"district": "서초구", "stores": ["서초점", "교대점", "방배점"]},
        {"district": "종로구", "stores": ["종로점", "광화문점"]},
        {"district": "마포구", "stores": ["합정점", "홍대점"]}
    ],
    "경기도": [
        {"district": "수원시", "stores": ["수원광교점", "수원역점"]},
        {"district": "고양시", "stores": ["일산점", "킨텍스점"]},
        {"district": "성남시", "stores": ["분당점", "판교점"]},
        {"district": "안양시", "stores": ["안양점", "평촌점"]}
    ],
    "인천광역시": [
        {"district": "부평구", "stores": ["부평역점", "부평점"]},
        {"district": "계양구", "stores": ["계양점", "작전점"]},
        {"district": "연수구", "stores": ["송도점", "연수점"]},
        {"district": "남동구", "stores": ["간석점", "구월점"]}
    ]
}

# HTML 페이지 렌더링
@app.route("/")
def store_selection():
    return render_template('html/storeSelection.html')

# 지역 데이터 API
@app.route("/api/regions")
def get_regions():
    return jsonify(regions)

if __name__ == "__main__":
    app.run(debug=True)
