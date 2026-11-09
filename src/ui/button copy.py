import pygame
class Button():
    def __init__(self,x,y,text,number,width,height,button_color,text_color,hover_darken_percent:float):
        self.text=text
        self.number=number
        self.color=button_color
        self.r,self.g,self.b=self.color
        self.hover_color=(self.r*hover_darken_percent,self.g*hover_darken_percent,self.b*hover_darken_percent)
        self.text_color=text_color
        self.rect=pygame.rect(x,y,width,height)
    def handle_event(self,event):
        if event.type==pygame.MOUSEMOTION:
            self.is_hovered=self.rect.collidepoint(event.pos)
        elif event.type==pygame.MOUSEBUTTONTODOWN and event.button==1:
            if self.is_hoverd:
                return True
        return False
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