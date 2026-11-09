BLESSINGS = {
    "Blessing of Battle": {"description": "Your target gains +10 Weapon Skill."},
    "Blessing of Breath": {
        "description": (
            "Your target does not need to breathe and ignores rules for Suffocation."
        )
    },
    "Blessing of Charisma": {"description": "Your target gains +10 Fellowship."},
    "Blessing of Conscience": {
        "description": (
            "Your target must pass an Average (+2 SL) Cool Test to break any of the"
            " strictures of your deity. If they fail, they are overcome with shame and"
            " do not take the action."
        )
    },
    "Blessing of Courage": {"description": "Your target gains +10 Willpower."},
    "Blessing of Finesse": {"description": "Your target gains +10 Dexterity."},
    "Blessing of Fortune": {
        "description": (
            "Your target may reroll their next failed Test. The reroll must stand."
        )
    },
    "Blessing of Grace": {"description": "Your target gains +10 Agility."},
    "Blessing of Hardiness": {"description": "Your target gains +10 Toughness."},
    "Blessing of Healing": {"description": "Your target heals +1 Wound."},
    "Blessing of The Hunt": {"description": "Your target gains +10 Ballistic Skill."},
    "Blessing of Might": {"description": "Your target gains +10 Strength."},
    "Blessing of Protection": {
        "description": (
            "Enemies must make an Average (+2 SL) Cool Test to attack your target as"
            " shame wells within for considering violence. If they fail, they must"
            " choose a different target, or a different Action."
        )
    },
    "Blessing of Recuperation": {
        "description": (
            "Your target may reduce the duration of 1 disease with which they are"
            " afflicted by 1 day. This prayer may only be attempted once per instance"
            " of a disease per person."
        )
    },
    "Blessing of Righteousness": {
        "description": "Your target’s weapon counts as Magical."
    },
    "Blessing of Savagery": {
        "description": (
            "When your target next inflicts a Critical Wound, roll twice and choose the"
            " best"
        )
    },
    "Blessing of Tenacity": {
        "description": "Your target may remove 1 Condition (except Besmirched)."
    },
    "Blessing of Wisdom": {"description": "Your target gains +10 Intelligence."},
    "Blessing of Wit": {"description": "Your target gains +10 Initiative."},
}


for blessing in BLESSINGS:
    BLESSINGS[blessing]["target"] = 1
    if blessing in ["Blessing of Healing", "Blessing of Recuperation"]:
        BLESSINGS[blessing]["range"] = "touch"
        BLESSINGS[blessing]["duration"] = "Instant"
    elif blessing in ["Blessing of Tenacity"]:
        BLESSINGS[blessing]["duration"] = "Instant"
    else:
        BLESSINGS[blessing]["range"] = "6 yards"
        BLESSINGS[blessing]["duration"] = "6 rounds"
