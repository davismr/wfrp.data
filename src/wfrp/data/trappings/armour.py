SHIELD_DATA = {
    "Buckler": {
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Common",
        "APs": 1,
        "Qualities": ["Shield"],
    },
    "Shield": {
        "Price": {"GC": 2},
        "Enc": 2,
        "Availability": "Common",
        "APs": 2,
        "Qualities": ["Shield"],
    },
    "Large Shield": {
        "Price": {"GC": 3},
        "Enc": 3,
        "Availability": "Common",
        "APs": 3,
        "Qualities": ["Shield"],
    },
}

for armour in SHIELD_DATA:
    armour["Group"] = "Shield"

LEATHER_DATA = {
    "Leather Coif": {
        "Price": {"GC": 2},
        "Enc": 0,
        "Availability": "Common",
        "Locations": ["Head"],
        "APs": 1,
        "Qualities": ["Partial"],
    },
    "Leather Jack": {
        "Price": {"GC": 3},
        "Enc": 1,
        "Availability": "Common",
        "Locations": ["Arms", "Body"],
        "APs": 1,
    },
    "Leather Jerkin": {
        "Price": {"GC": 2, "SS": 10},
        "Enc": 1,
        "Availability": "Common",
        "Locations": ["Body"],
        "APs": 1,
    },
    "Leather Leggings": {
        "Price": {"GC": 3},
        "Enc": 1,
        "Availability": "Common",
        "Locations": ["Legs"],
        "APs": 1,
    },
}

for armour in LEATHER_DATA:
    armour["Group"] = "Leather"

MAIL_DATA = {
    "Mail Chausses": {
        "Price": {"GC": 10},
        "Enc": 3,
        "Availability": "Scarce",
        "Locations": ["Legs"],
        "APs": 2,
        "Qualities": ["Flexible"],
    },
    "Mail Coat": {
        "Price": {"GC": 20},
        "Enc": 3,
        "Availability": "Scarce",
        "Locations": ["Arms", "Body"],
        "APs": 2,
        "Qualities": ["Flexible"],
    },
    "Mail Coif": {
        "Price": {"GC": 6},
        "Enc": 1,
        "Availability": "Scarce",
        "Locations": ["Head"],
        "APs": 2,
        "Qualities": ["Flexible", "Partial"],
    },
    "Mail Shirt": {
        "Price": {"GC": 16},
        "Enc": 2,
        "Availability": "Common",
        "Locations": ["Body"],
        "APs": 2,
        "Qualities": ["Flexible"],
    },
}

for armour in MAIL_DATA:
    armour["Group"] = "Mail"

PLATE_DATA = {
    "Bracers": {
        "Price": {"GC": 12},
        "Enc": 2,
        "Availability": "Rare",
        "Locations": ["Arms"],
        "APs": 2,
        "Qualities": ["Impenetrable", "Weakpoint"],
    },
    "Breastplate": {
        "Price": {"GC": 15},
        "Enc": 3,
        "Availability": "Scarce",
        "Locations": ["Body"],
        "APs": 2,
        "Qualities": ["Impenetrable", "Weakpoint"],
    },
    "Helm": {
        "Price": {"GC": 5},
        "Enc": 2,
        "Availability": "Rare",
        "Locations": ["Head"],
        "APs": 2,
        "Penalty": "–2 SL Perception",
        "Qualities": ["Impenetrable", "Weakpoint"],
    },
    "Open Helm": {
        "Price": {"GC": 3},
        "Enc": 1,
        "Availability": "Common",
        "Locations": ["Head"],
        "APs": 2,
        "Qualities": ["Partial"],
    },
    "Plate Leggings": {
        "Price": {"GC": 12},
        "Enc": 3,
        "Availability": "Rare",
        "Locations": ["Legs"],
        "APs": 2,
        "Qualities": ["Impenetrable", "Weakpoint"],
    },
}

for armour in PLATE_DATA:
    armour["Group"] = "Plate"

ARMOUR_DATA = SHIELD_DATA | LEATHER_DATA | MAIL_DATA | PLATE_DATA
