"""
LOCATION_DICT = {
    # --- 1F：施設・教室 ---
    "女子大浴場": "girls_public_bath",
    "男子大浴場": "boys_public_bath",
    "大温室": "great_greenhouse",
    "薬学室": "potions_room",
    "生物学室": "biology_room",
    "身だしなみ室": "grooming_room",
    "校長室": "headmasters_office",
    "購買室": "school_store",
    "大食堂": "great_dining_hall",
    "図書室1F": "library_1f",
    "備品倉庫": "supply_storage",
    "防衛学室": "defense_arts_room",
    "医務室": "infirmary",
    "職員室": "staff_room",

    # --- 1F：寮・屋外・門 ---
    "女子寮1F": "girls_dorm_1f",
    "男子寮1F": "boys_dorm_1f",
    "男性職員寮1F": "male_staff_dorm_1f",
    "女性職員寮1F": "female_staff_dorm_1f",
    "裏門": "back_gate",
    "裏門前": "in_front_of_back_gate",
    "正門前": "in_front_of_main_gate",
    "表門": "front_gate",
    "中庭": "courtyard",
    "職員棟前": "in_front_of_staff_building",
    "梟小屋(手紙)": "owlery",

    # --- 2F ---
    "女子寮2F": "girls_dorm_2f",
    "男子寮2F": "boys_dorm_2f",
    "男性職員寮2F": "male_staff_dorm_2f",
    "女性職員寮2F": "female_staff_dorm_2f",
    "古代語学室": "ancient_languages_room",
    "召喚学室": "summoning_room",
    "幻惑学室": "illusion_magic_room",
    "図書室2F": "library_2f",
    "錬金学室": "alchemy_room",
    "談話室": "common_room",
    "解呪学室": "curse_breaking_room",

    # --- 3F ---
    "女子寮3F": "girls_dorm_3f",
    "男子寮3F": "boys_dorm_3f",
    "占星学室": "astrology_room",
    "結界学室": "barrier_magic_room",
    "遊技室": "game_room",
    "転移学室": "teleportation_room",
    "変性学室": "transmutation_room",
    "廃教室": "abandoned_classroom",

    # --- 通路・階段（必要な場合） ---
    "廊下": "corridor",
    "階段": "stairs",
    "西階段踊り場": "west_stair_landing",
    "東階段踊り場": "east_stair_landing",
}
"""
"""
ロケーションに必要なもの
遷移先＝コネクションズ
"""

class Location:
    def __init__(self,name,connections):
        
        self.name=name
        self.connections=connections
    def set_propertys(self):
        pass