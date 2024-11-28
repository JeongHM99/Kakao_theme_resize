import os
from tkinter import Tk, filedialog, Button, messagebox, simpledialog
from PIL import Image

# 이미지 처리 규격 설정
IMAGE_CONFIGS = {
    "스플래시 가로": {
        "drawable-land-xhdpi": (1280, 720),
        "drawable-land-xxhdpi": (2560, 1440),
        "drawable-sw600dp-land": (2560, 1440),
    },
    "스플래시 세로": {
        "drawable-sw600dp": (1440, 2560),
        "drawable-xhdpi": (720, 1280),
        "drawable-xxhdpi": (1440, 2560),
    },
    "배경 이미지": {
        "drawable-sw600dp": (1440, 2880),
        "drawable-xxhdpi": (1440, 2880),
    },
    "채팅방 배경": {
        "drawable-sw600dp": (1440, 2880),
        "drawable-xxhdpi": (1440, 2880),
    },
    "기본프로필": {
        "drawable-nodpi": (320, 320),
        "drawable-xxhdpi": (240, 240),
    },
    "메인탭배경": {
        "drawable-sw600dp": (1440, 212),
        "drawable-xxhdpi": (1440, 212),
    },
    "받는말풍선1": {
        "drawable-xxhdpi": (0, 0),
    },
    "받는말풍선2": {
        "drawable-xxhdpi": (0, 0),
    },
    "보내는말풍선1": {
        "drawable-xxhdpi" : (0, 0),
    },
    "보내는말풍선2": {
        "drawable-xxhdpi" : (0, 0),
    },
    "잠금배경": {
        "drawable-sw600dp" : (1440, 1440),
        "drawable-xxhdpi" : (1440, 1440),
    },
    "잠금불릿1": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿2": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿3": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿4": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿체크1": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿체크2": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿체크3": {
        "drawable-xxhdpi" : (132, 132),
    },
    "잠금불릿체크4": {
        "drawable-xxhdpi" : (132, 132),
    },
    "친구추가": {
        "drawable-xxhdpi" : (126, 102),
    },
    "친구추가누름": {
        "drawable-xxhdpi" : (126, 102),
    },
    "메인탭아이콘1": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘누름1": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘2": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘누름2": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘3": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘누름3": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘4": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘누름4": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘5": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘누름5": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘call": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘call누름": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘game": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘game누름": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘find": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘find누름": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘piccoma": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    "메인탭아이콘piccoma누름": {
        "drawable-sw600dp" : (152, 152),
        "drawable-xxhdpi" : (152, 152),
    },
    # 추가 항목은 필요시 여기에 추가
}
# 출력 파일명 설정
OUTPUT_NAMES = {
    "스플래시 가로": "theme_splash_image",
    "스플래시 세로": "theme_splash_image",
    "배경 이미지": "theme_background_image",
    "채팅방 배경": "theme_chatroom_background_image",
    "기본프로필": {
        "drawable-nodpi": "theme_profile_01_image_full",  # "drawable-nodpi"는 full 이름으로 저장
        "drawable-xxhdpi": "theme_profile_01_image",     # "drawable-xxhdpi"는 기존 이름대로 저장
    },
    "메인탭배경": "theme_maintab_cell_image",
    "받는말풍선1": "theme_chatroom_bubble_you_01_image.9",
    "받는말풍선2": "theme_chatroom_bubble_you_02_image.9",
    "보내는말풍선1": "theme_chatroom_bubble_me_01_image.9",
    "보내는말풍선2": "theme_chatroom_bubble_me_02_image.9",
    "잠금배경": "theme_passcode_background_image",
    "잠금불릿1": "theme_passcode_01_image",
    "잠금불릿2": "theme_passcode_02_image",
    "잠금불릿3": "theme_passcode_03_image",
    "잠금불릿4": "theme_passcode_04_image",
    "잠금불릿체크1": "theme_passcode_01_checked_image",
    "잠금불릿체크2": "theme_passcode_02_checked_image",
    "잠금불릿체크3": "theme_passcode_03_checked_image",
    "잠금불릿체크4": "theme_passcode_04_checked_image",
    "친구추가": "theme_find_add_friend_button_image",
    "친구추가누름": "theme_find_add_friend_button_pressed_image",
    "메인탭아이콘1": "theme_maintab_ico_friends_image",
    "메인탭아이콘누름1": "theme_maintab_ico_friends_focused_image",
    "메인탭아이콘2": "theme_maintab_ico_chats_image",
    "메인탭아이콘누름2": "theme_maintab_ico_chats_focused_image",
    "메인탭아이콘3": "theme_maintab_ico_openchat_image",
    "메인탭아이콘누름3": "theme_maintab_ico_openchat_focused_image",
    "메인탭아이콘4": "theme_maintab_ico_shopping_image",
    "메인탭아이콘누름4": "theme_maintab_ico_shopping_focused_image",
    "메인탭아이콘5": "theme_maintab_ico_more_image",
    "메인탭아이콘누름5": "theme_maintab_ico_more_focused_image",
    "메인탭아이콘call": "theme_maintab_ico_call_image",
    "메인탭아이콘call누름": "theme_maintab_ico_call_focused_image",
    "메인탭아이콘game": "theme_maintab_ico_game_image",
    "메인탭아이콘game누름": "theme_maintab_ico_game_focused_image",
    "메인탭아이콘find": "theme_maintab_ico_find_image",
    "메인탭아이콘find누름": "theme_maintab_ico_find_focused_image",
    "메인탭아이콘piccoma": "theme_maintab_ico_piccoma_image",
    "메인탭아이콘piccoma누름": "theme_maintab_ico_piccoma_focused_image",
    # 추가 항목은 필요시 여기에 추가
}

# 이미지를 선택했는지 여부를 추적하기 위한 변수
selected_images = {}

def select_image(config_key):
    """사용자에게 이미지를 선택하도록 요청하는 함수."""
    file_path = filedialog.askopenfilename(
        title=f"'{config_key}' 이미지를 선택하세요",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    return file_path

def process_image(file_path, config_key, output_folder):
    """선택된 이미지를 주어진 규격에 맞게 리사이즈하고 저장하는 함수."""
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    config = IMAGE_CONFIGS.get(config_key, {})
    
    if config_key == "기본프로필":
        for folder, size in config.items():
            output_name = OUTPUT_NAMES["기본프로필"].get(folder, base_name)
            output_path = os.path.join(output_folder, folder)
            os.makedirs(output_path, exist_ok=True)

            img = Image.open(file_path)
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            output_path = os.path.join(output_path, f"{output_name}.png")
            img_resized.save(output_path)
            print(f"Saved: {output_path}")

    elif config_key in ["받는말풍선1", "받는말풍선2", "보내는말풍선1", "보내는말풍선2"]:
        for folder, size in config.items():
            output_name = OUTPUT_NAMES.get(config_key, base_name)
            output_path = os.path.join(output_folder, folder)
            os.makedirs(output_path, exist_ok=True)

            img = Image.open(file_path)
            output_path = os.path.join(output_path, f"{output_name}.png")
            img.save(output_path)
            print(f"Saved: {output_path}")

    else:
        output_name = OUTPUT_NAMES.get(config_key, base_name)
        for folder, size in config.items():
            output_path = os.path.join(output_folder, folder)
            os.makedirs(output_path, exist_ok=True)

            img = Image.open(file_path)
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            output_path = os.path.join(output_path, f"{output_name}.png")
            img_resized.save(output_path)
            print(f"Saved: {output_path}")

def create_button(window, text, config_key, output_folder, row, column):
    """버튼을 생성하고, 클릭 시 이미지 선택 및 처리 함수 호출"""
    button = Button(window, text=text, command=lambda: button_click(config_key, output_folder, button))
    button.grid(row=row, column=column, padx=10, pady=10, sticky="ew")
    
    # 이미지 선택 여부에 따라 버튼 색상 설정
    if config_key in selected_images:
        button.config(bg="lightgreen")  # 선택된 이미지가 있으면 'lightgreen'
    else:
        button.config(bg="lightcoral")  # 기본 색상은 'lightcoral'

def button_click(config_key, output_folder, button):
    """버튼 클릭 시 이미지 선택 후 처리하는 함수"""
    file_path = select_image(config_key)
    if file_path:
        process_image(file_path, config_key, output_folder)
        selected_images[config_key] = file_path  # 선택된 이미지를 딕셔너리에 기록
        button.config(bg="lightgreen")  # 버튼 색상 변경
    else:
        messagebox.showwarning("이미지 선택 오류", f"{config_key} 이미지를 선택하지 않았습니다.")

def main():
    """메인 함수로 사용자가 이미지를 선택하고 작업을 처리하는 흐름을 관리."""
    # Tkinter 루트 윈도우 생성
    root = Tk()
    root.title("테마 이미지 리사이즈 프로그램")
    
    # 팝업 창의 크기 설정 (너비 800px, 높이 500px)
    root.geometry("1000x500")
    
    # 사용자로부터 결과 폴더 이름을 입력받는 팝업창
    output_folder_name = simpledialog.askstring("결과 폴더 이름", "결과를 저장할 폴더 이름을 입력하세요:")
    if not output_folder_name:
        messagebox.showerror("입력 오류", "폴더 이름을 입력하지 않았습니다.")
        return

    output_folder = os.path.join(os.getcwd(), output_folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # 버튼 배치할 위치 설정
    row = 0
    column = 0
    
    # 각 이미지 항목에 대해 버튼을 생성
    for config_key in IMAGE_CONFIGS.keys():
        create_button(root, f"{config_key} 이미지 선택", config_key, output_folder, row, column)
        
        # 한 줄에 버튼을 두 개씩 배치하기 위해 column을 2씩 증가
        column += 1
        if column == 4:
            column = 0
            row += 1

    # Tkinter 이벤트 루프 시작
    root.mainloop()

if __name__ == "__main__":
    main()