import tkinter as tk
from tkinter import ttk


# 새로운 메뉴 선택 창을 띄우는 함수
def open_menu_selection():
    # 메뉴 선택 창 생성
    menu_window = tk.Toplevel()
    menu_window.title("메뉴 선택")
    menu_window.geometry("400x600")

    # 상단 네비게이션 바
    nav_frame = tk.Frame(menu_window, bg="white")
    nav_frame.pack(fill="x")

    categories = ["NEW!", "All", "클래식 프레즐", "스틱 프레즐", "핫도그 프레즐", "딥", "에이드", "커피"]
    selected_category = tk.StringVar(value=categories[1])  # 기본 카테고리는 'All'

    # 카테고리 탭 생성
    def create_nav_buttons():
        for idx, category in enumerate(categories):
            btn = tk.Button(nav_frame, text=category, font=("Arial", 10),
                            command=lambda cat=category: show_menu_items(cat),
                            fg="green" if category == selected_category.get() else "black")
            btn.grid(row=0, column=idx, padx=5, pady=5)

    # 메뉴 아이템 표시 프레임
    menu_frame = tk.Frame(menu_window, bg="white")
    menu_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # 메뉴 데이터 (예시 데이터로 구현)
    menu_items = {
        "All": [
            {"name": "오리지널 프레즐", "information": "굵은 정제소금을 뿌려 고소하고 담백한 맛이 특징인 프레즐", "price": "3,500원"},
            {"name": "아몬드 크림치즈 스틱", "information": "바삭한 아몬드 크런치 토핑이 올려진 스틱안에 따뜻한 크림치즈가 듬뿍! 부드럽고 달콤한 맛의 아몬드 크림치즈 스틱", "price": "5,000원"},
            {"name": "할라피뇨 치즈 핫도그", "information": "오동통한 소시지를 넣은 핫도그에 치즈와 할라피뇨가 어우러져 짭짤하고 매콤한 맛의 할라피뇨 치즈 핫도그", "price": "5,200"}
            # 추가 아이템들
        ],
        # 다른 카테고리도 비슷하게 추가
    }

    # 선택한 카테고리에 따라 메뉴 아이템 표시
    def show_menu_items(category):
        for widget in menu_frame.winfo_children():
            widget.destroy()

        items = menu_items.get(category, menu_items["All"])

        for item in items:
            item_frame = tk.Frame(menu_frame, bg="white", bd=1, relief="solid")
            item_frame.pack(fill="x", pady=5)

            name_label = tk.Label(item_frame, text=item["name"], font=("Arial", 12, "bold"))
            name_label.pack(anchor="w", padx=10, pady=2)

            size_price_label = tk.Label(item_frame,
                                        text=f"{item['size']} {item['price']} | {item['large_size']} {item['large_price']}",
                                        font=("Arial", 10))
            size_price_label.pack(anchor="w", padx=10, pady=2)

    create_nav_buttons()
    show_menu_items(selected_category.get())


# 테스트 실행을 위한 메인 윈도우 설정
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Auntie Anne's 매장 선택")
    root.geometry("400x600")

    # 매장 선택 예시 버튼
    select_store_button = tk.Button(root, text="매장 선택 후 메뉴 보기", command=open_menu_selection)
    select_store_button.pack(pady=50)

    root.mainloop()
