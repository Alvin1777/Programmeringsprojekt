

class Player():
    def __init__(self, player_name, character, house):
        self.player_name = player_name
        self.character = character
        self.player_house = house

    def print_info(self):
        print("name: ",self.player_name,"character choise: ", self.character, "player house : ",self.player_house)

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
        