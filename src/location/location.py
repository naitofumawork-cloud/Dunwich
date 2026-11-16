"""
ロケーションに必要なもの
遷移先＝コネクションズ
"""

class Location:
    def __init__(self,name,connections):
        self.name=name
        self.connections=connections