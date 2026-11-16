from .button import Button
from src.settings.settings import*

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
            
def set_text_buttons(button_list,text_list):
    text_list_count=0
    for button in button_list:
        button.set_text(text_list[text_list_count])
        text_list_count+=1
#ホバーチェックをボタンリストを使って呼び出しておく
#まずはレクトを任意の数作成してリストに入れる関数を作る
def call_handle_event_buttons(button_list,event):
    for button in button_list:
        return_code=button.handle_event(event)
        if return_code is not None:
            break
    return return_code