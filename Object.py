from classes import *

#Objects

    #Enemies
SkeletonEnemy = enemy("Skeleton", 20, 6, False)
ZombieEnemy = enemy("Zombie", 30, 4, False)
OrcEnemy = enemy("Orc", 10, 10, False)
GoblinEnemy = enemy("Goblin", 15, 7, False)
BatEnemy = enemy("Bat",2, 2, False)
SpiderEnemy = enemy("Spider", 10, 4, False)

SkeletonBoss = enemy("Skeleton King", 40, 10, True)
ZombieBoss = enemy("Zombie king", 45, 6, True)
OrcBoss = enemy("Orc Lord", 30, 10, True)
DragonBoss = enemy("Dragon", 50, 12, True)
BatBoss = enemy("Man Bat",20, 5, True)
SpiderBoss = enemy("Papa Spider", 35, 7, True)

    #Weapons

SteelSwordWeapon = weapons("Steel sword", 1, 5, 50, True)
WoodSwordWeapon = weapons("Wooden sword", 0.5, 1, 10, True)
AtgeirSpearWeapon = weapons("Atgeir spear", 3, 4, 75, True)
YariSpearWeapon = weapons("Yari spear", 3, 3, 45, True)
DanishAxeWeapon = weapons("Danish axe", 20, 0.1, 10, True)
BattleAxeWeapon = weapons("Battle axe", 2, 6, 60, True)
GolokSwordWeapon = weapons("Golok sword", 0.5, 5.5, 60, True)
DaodacSwordWeapon = weapons("Daodac Sword", 1, 8, 95, True)
DefaultDaggerWeapon = weapons("Rusty dagger", 3, 1, 1, True)

    #Items

potatoItem = items("Potato", 5, True, 2, False)
beefItem = items("Beef", 10, True, 5, False)
healingPoitionItem = items("Healing potion", 100, True, 100, False)
bronzeArtifactItem = items("Bronze artifact", 50, False, 0, False)
silverArtifactItem = items("Silver artifact", 100, False, 0, False)
goldArtifactItem = items("Gold artifact", 200, False, 0, False)
