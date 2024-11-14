let allData;

// 데이터를 보여주는 함수
const showData = (data) => {
    let productContainerString = "";

    // 데이터에서 하나씩 가져와서 HTML 문자열을 생성
    data.forEach(element => {
        let articleString = `
            <div class="menu-item">
                <img src="../img/${element.img}" alt="${element.name}">
                <div class="name">${element.name}</div>
            </div>`;
        productContainerString += articleString;
    });

    // .menu-container 클래스가 있는 요소에 HTML 문자열을 삽입
    const productContainerDiv = document.querySelector(".menu-container");
    if (productContainerDiv) {
        productContainerDiv.innerHTML = productContainerString;
    }
};

// 데이터를 설정하는 함수 (초기 데이터를 보관)
const setData = (data) => {
    allData = data; // 데이터를 전역 변수로 저장
    showData(data); // 데이터를 화면에 표시
};

// JSON 파일을 불러와 데이터를 설정하는 함수
const fetchData = () => {
    fetch('../js/menu.json')
        .then(response => response.json())
        .then(data => setData(data))
        .catch(error => console.error('Error loading JSON data:', error));
};

// 카테고리 필터링 함수
const filterCategory = (category) => {
    if (category === 'all') {
        // "전체" 선택 시 모든 데이터를 표시
        showData(allData);
    } else {
        // 선택한 카테고리에 해당하는 데이터만 필터링하여 표시
        const filteredData = allData.filter(item => item.category === category);
        showData(filteredData);
    }
};

// 페이지가 로드될 때 JSON 데이터를 로드하여 표시
document.addEventListener("DOMContentLoaded", () => {
    fetchData(); // JSON 파일에서 데이터 불러오기
});

// 버튼 클릭 시 호버 효과를 비활성화하는 함수
document.querySelectorAll('.category-bar button').forEach(button => {
    button.addEventListener('click', function() {
        // 클릭한 버튼에 'clicked' 클래스 추가
        this.classList.add('clicked');
        
        // 다른 버튼들의 'clicked' 클래스는 제거
        document.querySelectorAll('.category-bar button').forEach(b => {
            if (b !== this) {
                b.classList.remove('clicked');
            }
        });
    });
});