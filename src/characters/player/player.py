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
    def __init__(self,name,inventory:list,grade,level,location):
        self.name=name
        self.grade=grade
        self.credits=credits#授業の単位
        self.level=level
        self.location=location
        self.money=money
        self.inventory=inventory
        self.skills=[]
        self.event_progress=[]
        self.flags={
            "death_count":0,
            "death_count":0
        }
        
        self.counters={
            "kill_count":0,
            "death_count":0
            }   
    
    def handle_event(self,event):
        if event.type==pygame.MOUSEMOTION:
            self.is_hovered=self.rect.collidepoint(event.pos)
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.is_hovered:
                print(f"{self.text}ボタンが押されました")
                return self.number