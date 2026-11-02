import sys
import pygame
from pygame.locals import *
import json
import os
#ベースディレクトリ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

option_path = os.path.join(BASE_DIR, "config", "options.json")

# ファイルが存在するか確認してロード
if os.path.exists(option_path):
    with open(option_path, "r", encoding="utf-8") as f:
        option_data = json.load(f)
    print("設定データの読み込み成功:", option_data)
    print("設定データの読み込み成功:", option_data["SCREEN"])
else:
    print("ファイルが見つかりません:", option_path)
SCREEN_PROPERTY=option_data["SCREEN"]
SCREEN_WIDTH=SCREEN_PROPERTY["WIDTH"]
SCREEN_HEIGHT=SCREEN_PROPERTY["HEIGHT"]
TITLE=SCREEN_PROPERTY["CAPTION"]
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)



#フォントパス

FONT_PATH = os.path.join(BASE_DIR, "font", "NotoSansJP-VariableFont_wght.ttf")
pygame.init()
def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(TITLE)
    font=pygame.font.SysFont(FONT_PATH,25)
    while True:
        screen.fill((255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pass
if __name__=="__main__":
    main()

"""
ゲームループ
タイトル
モード選択
ゲーム～終了
モード
"""

