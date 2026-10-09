def get_random_talent(die_roll):
    while True:
        try:
            return TALENT_LIST[die_roll]
        except KeyError:
            die_roll += 1


TALENT_LIST = {
    2: "Acute Sense (Sight)",
    5: "Ambidextrous",
    7: "Artistic",
    10: "Attractive",
    12: "Briber",
    15: "Cardsharp",
    17: "Catfall",
    20: "Coolheaded",
    22: "Contortionist",
    25: "Flee!",
    27: "Gregarious",
    30: "Iron Jaw",
    32: "Lightning Reflexes",
    35: "Linguistics",
    37: "Marksman",
    40: "Mimic",
    42: "Night Vision",
    45: "Nimble-fingered",
    47: "Noble Blood",
    50: "Nose for Trouble",
    52: "Orientation",
    55: "Perfect Pitch",
    57: "Pure Soul",
    60: "Read/Write",
    62: "Resistant (Poison)",
    65: "Rover",
    67: "Savvy",
    70: "Sea Legs",
    72: "Sharp",
    75: "Stone Soup",
    77: "Strong Back",
    80: "Sturdy",
    82: "Suave",
    85: "Super Numerate",
    87: "Supportive",
    90: "Tinker",
    92: "Tunnel Fighter",
    95: "Very Resilient",
    97: "Very Strong",
    100: "Warrior Born",
}
