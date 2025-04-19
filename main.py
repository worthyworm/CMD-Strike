import os
import time

version = "alpha-test"
roundTime = 115
bombTime = 40
plantTime = 3
defuseTime = 10
defuseTimeKit = 5
scoreToWin = 13
teamSwitch = 12
roundsPlayed = 0
roundsMax = 24

maps = ["Mirage", "Dust 2", "Inferno", "Anubis", "Ancient", "Train"]

weapons = {
    "Glock-18" : {"damage" : 30, "cost" : 200, "penetration" : 47, "ammo" : 20, "magazines" : 6, "reload" : 2.2, "bounty" : 300, "side" : "T", "type" : "Pistol"},
    "USP-S" : {"damage" : 35, "cost" : 200, "penetration" : 51, "ammo" : 12, "magazines" : 2, "reload" : 2.2, "bounty" : 300, "side" : "CT", "type" : "Pistol"},
    "Dual-Berettas" : {"damage" : 38, "cost" : 400, "penetration" : 57, "ammo" : 30, "magazines" : 4, "reload" : 3.8, "bounty" : 300, "side" : "", "type" : "Pistol"},
    "P250" : {"damage" : 38, "cost" : 300, "penetration" : 64, "ammo" : 13, "magazines" : 2, "reload" : 2.2, "bounty" : 300, "side" : ""},
    "Five-SeveN" : {"damage" : 32, "cost" : 500, "penetration" : 92, "ammo" : 20, "magazines" : 5, "reload" : 2.2, "bounty" : 300, "side" : "CT", "type" : "Pistol"},
    "Tec-9" : {"damage" : 33, "cost" : 500, "penetration" : 90, "ammo" : 18, "magazines" : 5, "reload" : 2.5, "bounty" : 300, "side" : "T"},
    "Desert Eagle" : {"damage" : 73, "cost" : 700, "penetration" : 93, "ammo" : 7, "magazines" : 5, "reload" : 2.2, "bounty" : 300, "side" : "", "type" : "Pistol"},
    "MAC-10" : {},
    "MP9" : {},
    "MP5-SD" : {},
    "FAMAS" : {},
    "Galil AR" : {},
    "M4A1-S" : {},
    "M4A4" : {},
    "AK-47" : {},
    "SSG 08" : {},
    "AWP" : {},
    "Knife" : {},

}

teams = [{





}]