class Player():
    def __init__(self, playername, character, playerhouse, playerhealth):
        self.playername = playername
        self.charcter = character
        self.playerhouse = playerhouse
        self.playerhealth = playerhealth

class weapons():
    def __init__(self, weaponname):
        self.weaponname = weaponname


class items():
    def __init__(self, itemname):
        self.itemname = itemname


class enemy():
    def __init__(self, enemyname, enemyhealth):
        self.enemyname = enemyname
        self.enemyhealth = enemyhealth
        