import sys
import pygame
from pygame.locals import *
import json
import math
import os
import pygame._sdl2.video as sdl2_video  # SDL2のウィンドウ操作用
from src.ui.button import*
#モジュールインポート
#設定
from src.settings.settings import*
#ロケーション
from src.location.location import*
#uiモジュール
from src.ui.ui_manager import*
#savedata
from saves.load_save_data import*
#プレイヤー
from src.characters.player.player import*

test_text_list=["防衛術室へ向かう","薬学室へ向かう","生物学室へ向かう","錬金学室へ向かう","幻惑学室へ向かう","裏門へ向かう","森へ向かう","森へ向かう2"]
#ボタン名リストは現在地のコネクションズattributeから取得する
#test_text_list=["大広間へ向かう","薬学室へ向かう","生物学室へ向かう","防衛学室へ向かう","錬金学室へ向かう","幻惑学室へ向かう","裏門へ向かう","森へ向かう"]
test_game_events=[{"大広間へ向かう":"大広間へ向かう","test2":2}]

def load_location(save_data):
    location=save_data["player"]["location"]
    return location

def game_event_dispatcher(action,game_events):
    for game_event in game_events:
        if action == game_event:
            print(f"アクションとゲームイベントが一致しました{game_event['value']}")
#全てのロケーションを実体化させてリストに格納する
locations=[]
def create_locations(locations_list):
    for location_property in locations_list:
        locations.append(Location(location_property))
def load_save_data():
    pass
pygame.init()

#セーブデータjsonを読み込んで現在のロケーションを決定する
def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
    

    pygame.display.set_caption(TITLE)
    font=pygame.font.Font(FONT_PATH,25)
    #ボタン8個生成
    button_list=create_buttons(8,BLACK,GRAY,300,100,0.4)
    # print(button_list[0].color)

    rectA = pygame.Rect(100, 100, 100, 100)

    #文字貼り付けテスト
    test_text = "AA"
    text_surface = font.render(test_text, True, GREEN)  # (文字, 滑らかさ, 色)
    
    #ループ内の行動等を格納する変数この変数を読み込んで処理を変える
    aciton=""
    #プレイヤーインスタンス生成
    #セーブデータを引数にしてプレイヤークラスをインスタンス化
    #戻り値にそのインスタンスを返す関数が必要
    player=Player()
    
    while True:
        #ロケーションのセット
        save_data=load_save_data()
        location=load_location(save_data)
        
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
            action=call_handle_event_buttons(button_list,event)
            if action:
                print(action)
        game_event_dispatcher(action,test_game_events[0])
        #取り出されたイベントを処理させる
        
if __name__=="__main__":
    main()
    