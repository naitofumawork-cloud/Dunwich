import sys
import pygame
from pygame.locals import *
import json
import math
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

COLOR_PROPERTY=option_data["COLOR"]
#    "RED":{"r":255,"g":0,"b":0},
#色読み込み関数
def load_color(COLOR):
    color=COLOR_PROPERTY[COLOR]["r"],COLOR_PROPERTY[COLOR]["g"],COLOR_PROPERTY[COLOR]["b"]
    return color

RED=load_color("RED")
GREEN=load_color("GREEN")
BLUE=load_color("BLUE")
YELLOW=load_color("YELLOW")

PURPLE=load_color("PURPLE")
ORANGE=load_color("ORANGE")
WHITE=load_color("WHITE")
BLACK=load_color("BLACK")
GRAY=load_color("GRAY")



#フォントパス

FONT_PATH = os.path.join(BASE_DIR, "font", "NotoSansJP-VariableFont_wght.ttf")
#ボタン描画関数
def create_buttons(num,text_color,button_color,width,height,hover_darken_percent):
    button_lsit=[]
    for i in range(num):
        #    #テキスト、番号、長さ、高さ、ボタン背景の色、テキストの色、ホバー時にどの程度暗くするか
        #     def __init__(self,number,text_color,button_color,width,height,hover_darken_percent:float):
        button_lsit.append(Button(i+1,text_color,button_color,width,height,hover_darken_percent))
    return button_lsit
def draw_buttons(screen,button_lsit,font):
    for button in button_lsit:
        button.draw(screen,font)
# def draw_buttons(screen,button_lsit):
#     for i in button_lsit:
#         pygame.draw.rect(screen,i.color,i,)
#ボタンリストを受け取ってすべてのボタンに等間隔で中心座標を設定する
def set_position_buttons(button_list,startx,starty,pady,):#座標を一括設定するボタンリスト、エックス座標の開始位置、y座標の開始位置、ボタンの幅間隔
    global SCREEN_WIDTH
    SCREEN_WIDTH-startx
    #ボタンリストの長さは偶数限定
    half_len=len(button_list)//2#ボタンリストの長さの半分が入る
    left_set_count=0
    right_set_count=0
    for button in button_list:
        if left_set_count<half_len:
            button.set_position(startx,starty+pady*left_set_count)
            left_set_count+=1
        else:
            button.set_position(SCREEN_WIDTH-startx,starty+pady*right_set_count)
            right_set_count+=1
#テスト用テキストリスト
test_text_list=["test1","test2","test3","test4","test5","test6","test7","test8"]

def set_text_buttons(button_list,text_list):
    text_list_count=0
    for button in button_list:
        button.set_text(text_list[text_list_count])
        text_list_count+=1
#ホバーチェックをボタンリストを使って呼び出しておく
#まずはレクトを任意の数作成してリストに入れる関数を作る
def call_handle_event_buttons(button_list,event):
    for button in button_list:
        button.handle_event(event)



pygame.init()
def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
    

    pygame.display.set_caption(TITLE)
    font=pygame.font.SysFont(FONT_PATH,25)
    #ボタン8個生成
    button_list=create_buttons(8,BLACK,GRAY,300,100,0.1)
    print(button_list[0].color)

    rectA = pygame.Rect(100, 100, 100, 100)

    #文字貼り付けテスト
    test_text = "AA"
    text_surface = font.render(test_text, True, GREEN)  # (文字, 滑らかさ, 色)
    
    

    while True:
        screen.fill((255,255,255))
        #ボタン描画
        #ボタンの座標設定
        set_position_buttons(button_list,170,60,200)
        #ボタンにテキストを設定
        set_text_buttons(button_list,test_text_list)
        draw_buttons(screen,button_list,font)
        pygame.draw.rect(screen, (255, 0, 0),rectA)
        text_rect = text_surface.get_rect(center=rectA.center)
        
        #レクトとテキストの更新
        #レクトとテキストの紐づけはそれぞれをリスト化して走査して行えば行数削減可能

        screen.blit(text_surface, text_rect)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #全てのボタンインスタンスのイベントハンドル呼び出しを行う

            handle_event(
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

