

class Player():
    def __init__(self, player_name, player_character, player_house, character_name_title, character_name_surname, player_health, player_level):
        self.player_name = player_name
        self.character = player_character
        self.player_house = player_house
        self.character_name_title = character_name_title
        self.character_name_surname = character_name_surname
        self.player_health = player_health
        self.player_level = player_level

    def print_info(self):
        print("name: ",self.player_name,"character choice: ", self.character, "player house : ",self.player_house)

    def PrintPlayerName(self):
        print(self.character_name_title, self.player_name, self.character_name_surname)

class weapons():
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name


class items():
    def __init__(self, item_name):
        self.item_name = item_name


class enemy():
    def __init__(self, enemy_name, enemy_health, enemy_damage, is_boss):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_is_boss = is_boss
        