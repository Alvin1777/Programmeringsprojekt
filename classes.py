class Player():
    def __init__(self, player_name, player_character, player_house, character_name_title, character_name_surname, player_health, player_bank, player_xp_multiplier, player_damage_reduction, player_damage_multiplier, player_weapon_price_reduction, player_item_price_reduction):
        self.player_name = player_name
        self.character = player_character
        self.player_house = player_house
        self.character_name_title = character_name_title
        self.character_name_surname = character_name_surname
        self.player_health = player_health
        self.player_level = 0
        self.bank = player_bank
        self.xp_multi = player_xp_multiplier
        self.damage_reduction = player_damage_reduction
        self.damage_multiplier = player_damage_multiplier
        self.current_xp = 0
        self.boss_spawn = 0
        self.weapon_price_reduction = player_weapon_price_reduction
        self.item_price_reduction = player_item_price_reduction


    def printPlayerName(self):
        print(self.character_name_title, self.player_name, self.character_name_surname)

class weapons():
    def __init__(self, weapon_name, attack_speed, weapon_damage, weapon_value, isWeapon):
        self.weapon_name = weapon_name
        self.attack_speed = attack_speed
        self.weapon_damage = weapon_damage
        self.weapon_value = weapon_value
        self.isWeapon = isWeapon

    def showWeaponStats(self):
        print(f"{self.weapon_name}, Damage: {self.weapon_damage}, Price: {self.weapon_value}")
        

class items():
    def __init__(self, item_name, item_value, isHealingItem, healing_power, isWeapon):
        self.item_name = item_name
        self.item_value = item_value
        self.isHealingItem = isHealingItem
        self.healing_power = healing_power
        self.isWeapon = isWeapon

    def showItemStats(self):
        print(f"{self.item_name}, Healing: {self.healing_power}, Price: {self.item_value}")


class enemy():
    def __init__(self, enemy_name, enemy_health, enemy_damage, is_boss):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_is_boss = is_boss
        