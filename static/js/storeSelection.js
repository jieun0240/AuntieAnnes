document.addEventListener('DOMContentLoaded', () => {
    // JSON 파일에서 지역 데이터 불러오기
    let regions = {};
    
    fetch('/static/js/store.json') // JSON 파일 경로
        .then(response => response.json())
        .then(data => {
            regions = data;
            initializeSelectors();
        })
        .catch(error => console.error('Error loading regions data:', error));

    // 도/시 선택 시 구/군 목록 업데이트
    const citySelect = document.querySelector('#select-store-item select:first-child');
    citySelect.addEventListener('change', (event) => {
        const city = event.target.value;
        updateDistricts(city, regions);
    });

    // 구/군 선택 시 매장 목록 업데이트
    const districtSelect = document.querySelector('#select-store-item select:last-child');
    districtSelect.addEventListener('change', (event) => {
        const city = citySelect.value;
        const district = event.target.value;
        updateStores(city, district, regions);
    });

    // 도/시와 구/군 선택 초기화
    function initializeSelectors() {
        updateCities(regions);
        updateDistricts("도/시 선택", regions);
        updateStores("도/시 선택", "구/군 선택", regions);
    }

    // 도/시 목록 업데이트
    function updateCities(regions) {
        citySelect.innerHTML = '<option>도/시 선택</option>'; // 기본 옵션

        // 모든 도/시 추가
        Object.keys(regions).forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            citySelect.appendChild(option);
        });
    }

    // 구/군 목록 업데이트
    function updateDistricts(city, regions) {
        districtSelect.innerHTML = '<option>구/군 선택</option>'; // 기본 옵션

        if (city === "도/시 선택") return;

        const districts = regions[city] || [];
        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district.district;
            option.textContent = district.district;
            districtSelect.appendChild(option);
        });
    }

    // 매장 목록 업데이트
    function updateStores(city, district, regions) {
        const storeListContainer = document.querySelector('.store-search');
        storeListContainer.innerHTML = ''; // 기존 매장 목록 초기화
    
        if (district === "구/군 선택") return;
    
        const selectedDistrict = regions[city]?.find(item => item.district === district);
        if (selectedDistrict) {
            // 매장 데이터를 반복하며 각각의 <div> 생성
            selectedDistrict.stores.forEach(store => {
                // 개별 매장 정보를 감쌀 div 생성
                const storeWrapper = document.createElement('div');
                storeWrapper.className = 'store-item-wrapper'; // 감싸는 div 클래스
                storeWrapper.innerHTML = `
                    <div class="store-item">${store}</div>
                `;
                // 부모 컨테이너에 추가
                storeListContainer.appendChild(storeWrapper);
            });
        }
    }
});