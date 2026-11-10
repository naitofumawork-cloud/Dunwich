import pygame
#ボダンに必要な要素
""""
ボタンに貼るテキスト
ボタンの名前描画座標ボタンのたかさ長さ文字の色背景色ホバー時の色が何パーセント暗くなるか
"""
class Button():
    #テキスト、番号、長さ、高さ、ボタン背景の色、テキストの色、ホバー時にどの程度暗くするか
    def __init__(self,number,text_color,button_color,width,height,hover_darken_percent:float):
        self.text=""
        self.x=0
        self.y=0
        self.number=number
        self.text_color=text_color
        self.color=button_color

        self.rect=pygame.Rect(0,0,width,height)
        self.r,self.g,self.b=self.color
        self.hover_color=(self.r*hover_darken_percent,self.g*hover_darken_percent,self.b*hover_darken_percent)
        

    def handle_event(self,event):
        if event.type==pygame.MOUSEMOTION:
            self.is_hovered=self.rect.collidepoint(event.pos)
        elif event.type==pygame.MOUSEBUTTONTODOWN and event.button==1:
            if self.is_hoverd:
                return True
        return False
    def set_position(self,x,y):
        self.x=x
        self.y=y
    def set_text(self,text):
        self.text=text
    def draw(self,surface,font):
        current_color = self.hover_color if self.is_hovered else self.color
        # ボタン本体の描画
        pygame.draw.rect(surface, current_color, self.rect)
        pygame.draw.rect(surface, (50, 50, 50), self.rect, 2)  # 枠線
        # テキストの描画
        if self.text:
            text_surf = font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)