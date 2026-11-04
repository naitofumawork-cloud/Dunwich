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
        