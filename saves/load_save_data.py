import os
import json
from  pathlib import Path 
#ベースディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
save_datapath=Path(__file__).parent/"save_data.json"
def load_save_data():
    with open(save_datapath,"r",encoding="utf-8")as f:
        save_data=json.load(f)
        return save_data
    

# # config\options.json
# # ファイルが存在するか確認してロード
# if os.path.exists(option_path):
#     with open(option_path, "r", encoding="utf-8") as f:
#         option_data = json.load(f)
#     print("設定データの読み込み成功:", option_data)
#     print("設定データの読み込み成功:", option_data["SCREEN"])
# else:
#     print("ファイルが見つかりません:", option_path)
# SCREEN_PROPERTY=option_data["SCREEN"]
# SCREEN_WIDTH=SCREEN_PROPERTY["WIDTH"]
# SCREEN_HEIGHT=SCREEN_PROPERTY["HEIGHT"]
# TITLE=SCREEN_PROPERTY["CAPTION"]
# SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
# COLOR_PROPERTY=option_data["COLOR"]
# def load_color(COLOR):
#     color=COLOR_PROPERTY[COLOR]["r"],COLOR_PROPERTY[COLOR]["g"],COLOR_PROPERTY[COLOR]["b"]
#     return color

# RED=load_color("RED")
# GREEN=load_color("GREEN")
# BLUE=load_color("BLUE")
# YELLOW=load_color("YELLOW")

# PURPLE=load_color("PURPLE")
# ORANGE=load_color("ORANGE")
# WHITE=load_color("WHITE")
# BLACK=load_color("BLACK")
# GRAY=load_color("GRAY")
