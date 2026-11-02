import sys
import pygame
from pygame.locals import *
from src.screens.config.config import*#設定ファイル
from src.screens.utils import*
from src.screens.controlmanager import*
pygame.init()
def main():
    #ゲームのプロパティ値を管理する目的にインスタンスが必要か？
    #今はタイトルにいる？誰のターン？誰が何を持っている？等
    
    #ゲームステータスをタイトルに初期化
    app_state="title"
    #コントロールmanagerのオブジェクト化
    ctrlmanager=ControlManager(app_state)
    while True:
            app_state=ctrlmanager.call_control()
            #コントロールmanagerが現在のステータスを元に固有処理を実行結果を返す
            
            print("app state is>>"+str(app_state))
if __name__=="__main__":
    main()

"""
ゲームループ
タイトル
モード選択
ゲーム～終了
モード
"""

