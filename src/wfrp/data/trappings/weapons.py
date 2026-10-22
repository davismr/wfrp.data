BASIC_DATA = {
    "Dagger": {
        "Price": {"SS": 16},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
    },
    "Knife": {
        "Price": {"SS": 8},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 1],
        "Qualities": ["Undamaging"],
    },
    "Hand Weapon": {
        "Price": {"GC": 2},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 4],
        "Qualities": ["Unbalanced"],
    },
    "Improvised Weapon": {
        "Damage": ["SB", 1],
        "Qualities": ["Unbalanced", "Undamaging"],
    },
    "Net": {
        "Price": {"SS": 6},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Short",
        "Qualities": ["Defensive", "Inflict (Entangled 50)"],
    },
    "Sword": {
        "Price": {"GC": 4},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 4],
    },
}

for weapon in BASIC_DATA:
    weapon["Group"] = "Basic"

BRAWLING_DATA = {
    "Garrote": {
        "Two-Handed": True,
        "Price": {"SS": 1},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "Personal",
        "Damage": ["SB", 2],
        "Qualities": ["Inflict (Entangled your Strength)", "Undamaging"],
    },
    "Knuckledusters": {
        "Price": {"SS": 2, "BP": 6},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 2],
    },
    "Unarmed": {
        "Enc": 0,
        "Reach": "Personal",
        "Damage": ["SB", 0],
        "Qualities": ["Undamaging"],
    },
}

for weapon in BRAWLING_DATA:
    weapon["Group"] = "Brawling"

CAVALRY_DATA = {
    "Cavalry Hammer": {
        "Two-Handed": True,
        "Price": {"GC": 4},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Pummel"],
    },
    "Lance": {
        "Price": {"GC": 1},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": "Very Long",
        "Damage": ["SB", 6],
        "Qualities": ["Damaging", "Impale"],
    },
}

for weapon in CAVALRY_DATA:
    weapon["Group"] = "Cavalry"

FENCING_DATA = {
    "Buckler": {
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 1],
        "Qualities": ["Parry", "Undamaging"],
    },
    "Foil": {
        "Price": {"GC": 5},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Average",
        "Damage": ["SB", 3],
        "Qualities": ["Fast", "Impale", "Precise", "Undamaging"],
    },
    "Main Gauche": {
        "Price": {"GC": 1},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": "Short",
        "Damage": ["SB", 2],
        "Qualities": ["Defensive", "Impale", "Parry"],
    },
    "Rapier": {
        "Price": {"GC": 5},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Fast", "Impale"],
    },
    "Sword-breaker": {
        "Price": {"GC": 1, "SS": 2, "BP": 6},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "Short",
        "Damage": ["SB", 1],
        "Qualities": ["Defensive", "Parry", "Trap Blade"],
    },
}

for weapon in FENCING_DATA:
    weapon["Group"] = "Fencing"

FLAIL_DATA = {
    "Flail": {
        "Price": {"GC": 2},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Average",
        "Damage": ["SB", 4],
        "Qualities": ["Pummel", "Wrap", "Unbalanced"],
    },
    "Grain Flail": {
        "Two-Handed": True,
        "Price": {"SS": 5},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 3],
        "Qualities": ["Pummel", "Imprecise"],
    },
    "Military Flail": {
        "Two-Handed": True,
        "Price": {"GC": 3},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Damaging", "Pummel", "Wrap", "Unbalanced"],
    },
    "Whip": {
        "Price": {"SS": 5},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Very Long",
        "Damage": ["SB", 2],
        "Qualities": ["Wrap", "Unbalanced", "Undamaging"],
    },
}

for weapon in FLAIL_DATA:
    weapon["Group"] = "Flail"

POLEARM_DATA = {
    "Halberd": {
        "Price": {"GC": 2},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Defensive", "Hack", "Impale"],
    },
    "Pike": {
        "Price": {"SS": 18},
        "Enc": 4,
        "Availability": "Rare",
        "Reach": "Massive",
        "Damage": ["SB", 4],
        "Qualities": ["Impale"],
    },
    "Quarterstaff": {
        "Price": {"SS": 3},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 3],
        "Qualities": ["Defensive", "Pummel", "Undamaging"],
    },
    "Spear": {
        "Price": {"SS": 15},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Very Long",
        "Damage": ["SB", 4],
        "Qualities": ["Fast", "Impale"],
    },
}

for weapon in POLEARM_DATA:
    weapon["Group"] = "Polearm"
    weapon["Two-Handed"] = True

TWO_HANDED_DATA = {
    "Bastard Sword": {
        "Price": {"GC": 10},
        "Enc": 2,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Damaging", "Defensive"],
    },
    "Great Axe": {
        "Price": {"GC": 4},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 6],
        "Qualities": ["Damaging", "Hack", "Unbalanced"],
    },
    "Pick": {
        "Price": {"GC": 2},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Damaging", "Penetrating", "Unbalanced"],
    },
    "Warhammer": {
        "Price": {"GC": 4},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 6],
        "Qualities": ["Damaging", "Pummel", "Unbalanced"],
    },
    "Zweihänder": {
        "Price": {"GC": 16},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Damaging", "Hack"],
    },
}

for weapon in TWO_HANDED_DATA:
    weapon["Group"] = "Two-Handed"
    weapon["Two-Handed"] = True


BLACKPOWDER_DATA = {
    "Blunderbuss": {
        "Two-Handed": True,
        "Price": {"GC": 10},
        "Enc": 2,
        "Availability": "Scarce",
        "Reach": 20,
        "Damage": [8],
        "Qualities": [
            "Blast 3",
            "Dangerous",
            "Reload 2",
        ],
    },
    "Handgun": {
        "Two-Handed": True,
        "Price": {"GC": 16},
        "Enc": 2,
        "Availability": "Scarce",
        "Reach": 40,
        "Damage": [10],
        "Qualities": ["Reload 3"],
    },
    "Pistol": {
        "Price": {"GC": 20},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": 20,
        "Damage": [9],
        "Qualities": ["Pistol", "Reload 2"],
    },
}

for weapon in BLACKPOWDER_DATA:
    weapon["Group"] = "Blackpowder"
    weapon["Qualities"].extend(["Blackpowder", "Damaging"])

BOW_DATA = {
    "Bow": {
        "Price": {"GC": 4},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 50,
        "Damage": ["SB", 4],
    },
    "Longbow": {
        "Price": {"GC": 8},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": 60,
        "Damage": ["SB", 4],
        "Qualities": ["Damaging"],
    },
    "Shortbow": {
        "Price": {"GC": 3},
        "Enc": 1,
        "Availability": "Common",
        "Reach": 40,
        "Damage": ["SB", 3],
    },
}

for weapon in BOW_DATA:
    weapon["Group"] = "Bow"
    weapon["Two-Handed"] = True

CROSSBOW_DATA = {
    "Crossbow": {
        "Two-Handed": True,
        "Price": {"GC": 5},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 50,
        "Damage": [9],
        "Qualities": ["Reload 1"],
    },
    "Crossbow Pistol": {
        "Price": {"GC": 6},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": 20,
        "Damage": [7],
        "Qualities": ["Pistol", "Reload 1"],
    },
    "Heavy Crossbow": {
        "Two-Handed": True,
        "Price": {"GC": 8},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": 60,
        "Damage": [10],
        "Qualities": ["Reload 2"],
    },
}

for weapon in CROSSBOW_DATA:
    weapon["Group"] = "Crossbow"

ENGINEERING_DATA = {
    "Repeater Handgun": {
        "Two-Handed": True,
        "Price": {"GC": 50},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": 40,
        "Damage": [10],
        "Qualities": ["Repeater 4", "Dangerous", "Reload 5"],
    },
    "Repeater Pistol": {
        "Price": {"GC": 40},
        "Enc": 1,
        "Availability": "Rare",
        "Reach": 20,
        "Damage": [9],
        "Qualities": ["Pistol", "Repeater 4", "Dangerous", "Reload 4"],
    },
    "Hochland Long Rifle": {
        "Two-Handed": True,
        "Price": {"GC": 100},
        "Enc": 3,
        "Availability": "Exotic",
        "Reach": 100,
        "Damage": [10],
        "Qualities": [
            "Precise",
            "Reload 4",
        ],
    },
}

for weapon in ENGINEERING_DATA:
    weapon["Group"] = "Engineering"
    weapon["Qualities"].extend(["Blackpowder", "Damaging"])

ENTANGLING_DATA = {
    "Bolas": {
        "Price": {"SS": 10},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "SB×3",
        "Damage": ["SB", 3],
        "Qualities": ["Inflict (Entangled 35)", "Inflict (Prone)", "Undamaging"],
    },
    "Lasso": {
        "Two-Handed": True,
        "Price": {"SS": 6},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "SB*2",
        "Qualities": ["Inflict (Entangled 45)"],
    },
    "Net": {
        "Price": {"SS": 6},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "SB*2",
        "Qualities": ["Inflict (Entangled 45)"],
    },
}

for weapon in ENTANGLING_DATA:
    weapon["Group"] = "Entangling"

EXPLOSIVES_DATA = {
    "Bomb": {
        "Price": {"GC": 3},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "SB",
        "Damage": [12],
        "Qualities": ["Blast 5", "Inflict (Deafened)", "Dangerous"],
    },
    "Incendiary": {
        "Price": {"GC": 1},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": "SB",
        "Damage": [8],
        "Qualities": ["Blast 4", "Inflict (Ablaze)", "Dangerous"],
    },
}

for weapon in EXPLOSIVES_DATA:
    weapon["Group"] = "Explosives"
    weapon["Qualities"].extend(["Blackpowder", "Damaging"])

SLING_DATA = {
    "Sling": {
        "Price": {"SS": 1},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 40,
        "Damage": [6],
    },
    "Staff Sling": {
        "Two-Handed": True,
        "Price": {"SS": 4},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 50,
        "Damage": [7],
    },
}

for weapon in SLING_DATA:
    weapon["Group"] = "Sling"

THROWING_DATA = {
    "Javelin": {
        "Price": {"SS": 10, "BP": 6},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "SB×3",
        "Damage": ["SB", 3],
        "Qualities": ["Impale"],
    },
    "Rock": {
        "Enc": 0,
        "Availability": "Common",
        "Reach": "SB×3",
        "Damage": ["SB", 1],
        "Qualities": ["Undamaging"],
    },
    "Throwing Axe": {
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "SB×2",
        "Damage": ["SB", 3],
        "Qualities": ["Hack"],
    },
    "Throwing Knife": {
        "Price": {"SS": 18},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": "SB×2",
        "Damage": ["SB", 2],
    },
}

for weapon in THROWING_DATA:
    weapon["Group"] = "Throwing"

BLACKPOWDER_AMMO_DATA = {
    "Bullet and Powder (12)": {
        "Price": {"SS": 3, "BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Impale", "Penetrating"],
    },
    "Improvised Shot and Powder": {
        "Price": {"BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Damage": [-1],
        "Range": "Half weapon",
    },
    "Small Shot and Powder (12)": {
        "Price": {"SS": 3, "BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Blast +1"],
    },
}

for weapon in BLACKPOWDER_AMMO_DATA:
    weapon["Group"] = "Blackpowder and Engineering"

BOW_AMMO_DATA = {
    "Arrow (12)": {
        "Price": {"SS": 5},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Impale"],
    },
    "Elf Arrow": {
        "Price": {"SS": 6},
        "Enc": 0,
        "Availability": "Exotic",
        "Range": "+10",
        "Qualities": ["Impale"],
    },
}

for weapon in BOW_AMMO_DATA:
    weapon["Group"] = "Bow"

CROSSBOW_AMMO_DATA = {
    "Bolt (12)": {
        "Group": "Crossbow",
        "Price": {"SS": 5},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Impale"],
    },
}

SLING_AMMO_DATA = {
    "Lead Bullet (12)": {
        "Price": {"BP": 4},
        "Enc": 0,
        "Availability": "Common",
        "Range": "-10",
        "Damage": [1],
        "Qualities": ["Pummel"],
    },
    "Stone Bullet (12)": {
        "Price": {"BP": 1},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Pummel"],
    },
}

for weapon in SLING_AMMO_DATA:
    weapon["Group"] = "Sling"

MELEE_WEAPONS_DATA = (
    BASIC_DATA
    | CAVALRY_DATA
    | FENCING_DATA
    | BRAWLING_DATA
    | FLAIL_DATA
    | POLEARM_DATA
    | TWO_HANDED_DATA
)

RANGED_WEAPONS_DATA = (
    BLACKPOWDER_DATA
    | BOW_DATA
    | CROSSBOW_DATA
    | ENGINEERING_DATA
    | ENTANGLING_DATA
    | EXPLOSIVES_DATA
    | SLING_DATA
    | THROWING_DATA
)

AMMUNITION_DATA = (
    BLACKPOWDER_AMMO_DATA | BOW_AMMO_DATA | CROSSBOW_AMMO_DATA | SLING_AMMO_DATA
)

WEAPONS_DATA = MELEE_WEAPONS_DATA | RANGED_WEAPONS_DATA
