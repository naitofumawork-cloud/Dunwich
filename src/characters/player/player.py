import pygame
#プレイヤーに必要な要素
"""
名前=name
学年=grade
単位=credits
レベル=level
現在地=location
所持金=money
所持品inventory
所持品[]#アイテムの種別はアイテムインスタンスのもつカテゴリattributeの値で管理する
    初心者の杖.type="wand"
    銀の鎧.type="armor"
skills
習得したスキル[各呪文の習熟度の情報も入っている]#上記と同様
event_progress
各イベントの進行状態
フラグflag
カウンターcounter[]
"""
class Player():
    #テキスト、番号、長さ、高さ、ボタン背景の色、テキストの色、ホバー時にどの程度暗くするか
    def __init__(self,name,inventory:list,grade,level,location,money,skills:list,event_progress,flags:dict,counters:dict):
        self.rest()
    def rest(self):
        self.name="マーク"
        self.grade=1
        self.credits=0
        self.level=1
        self.location=""
        self.money=100
        self.inventory=[]
        self.skills=[]
        self.event_progress=[]
        self.flags=[]
        self.counters=[]
    def load_save_data(save_data):
        
        pass
        
    def handle_event(self,event):
        if event.type==pygame.MOUSEMOTION:
            self.is_hovered=self.rect.collidepoint(event.pos)
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.is_hovered:
                print(f"{self.text}ボタンが押されました")
                return self.number