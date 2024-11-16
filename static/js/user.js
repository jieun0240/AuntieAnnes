const userName = "김지은";
const userEmail = "jieun@example.com";
const userLevel = "Silver";

document.getElementById("user-name").textContent = userName;
document.getElementById("account-name").textContent = userName;
document.getElementById("account-email").textContent = userEmail;
document.getElementById("account-level").textContent = userLevel;

function editProfile() {
    alert("프로필 수정 페이지로 이동합니다.");
}

function logout() {
    alert("로그아웃 되었습니다.");
    // 실제 로그아웃 로직 필요
}
