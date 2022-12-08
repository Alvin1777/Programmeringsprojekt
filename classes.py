

class Player():
    def __init__(self, player_name, character, player_house, player_health):
        self.player_name = player_name
        self.character = character
        self.player_house = player_house
        self.player_health = player_health

class weapons():
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name


class items():
    def __init__(self, item_name):
        self.item_name = item_name


class enemy():
    def __init__(self, enemy_name, enemy_health):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        