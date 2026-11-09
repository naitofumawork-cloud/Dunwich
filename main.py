import sys
import pygame
from pygame.locals import *
import json
import os
import pygame._sdl2.video as sdl2_video  # SDL2のウィンドウ操作用
from src.ui.button import*
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
#ボタン描画関数
def create_button(num):
    for i in num:
        button=Button()
#まずはレクトを任意の数作成してリストに入れる関数を作る
pygame.init()
def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
    rectA = pygame.Rect(100, 100, 100, 100)

    pygame.display.set_caption(TITLE)
    font=pygame.font.SysFont(FONT_PATH,25)
    while True:
        screen.fill((255,255,255))
        #ボタン描画
        pygame.draw.rect(screen, (255, 0, 0),rectA)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pass
if __name__=="__main__":
    main()

"""
ボタンを画面に8個用意して
描画する
左右で四個ずつ
ゲーム開始
前回の情報を読み込んでインスタンスを生成
移動のたびにキャラのプロパティの値を書き換える
"""

