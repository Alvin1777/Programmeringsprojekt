

class Player():
    def __init__(self, player_name, player_character, player_house, character_name_title, character_name_surname, player_health, player_level, inventory_size, player_bank, player_xp_multiplier, player_damage_reduction, player_damage_multiplier, player_weapon_price_reduction, player_item_price_reduction):
        self.player_name = player_name
        self.character = player_character
        self.player_house = player_house
        self.character_name_title = character_name_title
        self.character_name_surname = character_name_surname
        self.player_health = player_health
        self.player_level = player_level
        self.inventory_size = inventory_size
        self.bank = player_bank
        self.xp_multi = player_xp_multiplier
        self.damage_reduction = player_damage_reduction
        self.damage_multiplier = player_damage_multiplier
        self.current_xp = 0
        self.boss_spawn = 0
        self.weapon_price_reduction = player_weapon_price_reduction
        self.item_price_reduction = player_item_price_reduction


    def print_info(self):
        print("Name: ",self.player_name,"Character Choice: ", self.character, "Player House: ",self.player_house,"Player Character Name: ", self.character_name_title,"Player Character Surname: ", self.character_name_surname,"Player Health: ", self.player_health,"Player Level: ", self.player_level)

    def PrintPlayerName(self):
        print(self.character_name_title, self.player_name, self.character_name_surname)

class weapons():
    def __init__(self, weapon_name, attack_speed, weapon_damage, weapon_value):
        self.weapon_name = weapon_name
        self.attack_speed = attack_speed
        self.weapon_damage = weapon_damage
        self.weapon_value = weapon_value

class items():
    def __init__(self, item_name, item_value, isHealingItem, healing_power):
        self.item_name = item_name
        self.item_value = item_value
        self.isHealingItem = isHealingItem
        self.healing_power = healing_power


class enemy():
    def __init__(self, enemy_name, enemy_health, enemy_damage, is_boss):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_is_boss = is_boss
        