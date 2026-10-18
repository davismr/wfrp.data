LORE_NURGLE = {
    "Festering Inflammation": {
        "CN": 5,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "You conjure up septic fluids in the wounds of your opponent. One of the"
            " target’s Wounds becomes a Festering Wound."
        ),
    },
    "Miasma of Pestilence": {
        "CN": 6,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "A thin mist gathers around you. All living creatures within the Area of"
            " Effect must pass a Hard (-2 SL) Endurance Test or suffer from the Nausea"
            " Symptom (see page 182). Those dedicated to Nurgle, and skaven plague"
            " monks, are not affected."
        ),
    },
    "Stream of Corruption": {
        "CN": 9,
        "range": "Special",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "Your maw distends horrifically before you vomit forth a foul stream of"
            " diseased filth and horror. Immediately make an Unopposed Acid- and"
            " Poison-type Breath attack (see page 357). It counts as a magic missile"
            " with a Damage equal to your Toughness Bonus, and it ignores Armour"
            " Points. Further, any targets that take more than their TB in Wounds must"
            " pass a Challenging (+0 SL) Endurance Test or contract Blood Rot (see page"
            " 179)."
        ),
    },
}

LORE_SLAANESH = {
    "Acquiescence": {
        "CN": 5,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Your magic pierces deep within your target, flooding their senses with"
            " strange, euphoric sensations. At the start of each Round, the target must"
            " make a Challenging (+0 SL) Endurance Test. If they fail, they lose their"
            " Move and Action as they are overwhelmed with blissful sensation."
        ),
    },
    "From Pain, Pleasure": {
        "CN": 6,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You confound the target’s senses, transforming pain to pleasure. The"
            " target gains the Painless Creature Trait (see page 360) for the duration"
            " of the Spell. As they endure injuries, they experience a wave of"
            " pleasurable sensation. Should they suffer a Critical Wound, they must"
            " pass an Average (+2 SL) Endurance Test or drop their weapons, standing"
            " Helplessly as their enemies rain blows down upon them, lost in the"
            " ecstatic rending of their own flesh."
        ),
    },
    "Phantasmagoria": {
        "CN": 8,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "In response to your invocation, unearthly visions of beguiling and"
            " fearsome creatures fill the area of effect, giving you and all allies the"
            " Distracting Creature Trait (see page 358) for the duration of the Spell."
            " Targets do not distract one another."
        ),
    },
}

LORE_TZEENTCH = {
    "Boon of Tzeentch": {
        "CN": 9,
        "range": "You",
        "target": "You",
        "duration": "Intelligence Bonus days",
        "description": (
            "The Changer of the Ways twists your mind, granting you access to arcane"
            " knowledge. Choose one Spell from any Lore. For the Duration, you may cast"
            " it as if you had memorised it, but may not record it in a grimoire. If"
            " you channel to cast the new Spell, you may use either Channelling (Dhar)"
            " or the Channelling Skill appropriate to the Spell, should you possess it."
            " If you suffer a Miscast when casting this new Spell, Boon of Tzeentch"
            " quits your mind in disgust, and also erases itself from your grimoire"
            " should it have allowed itself to be recorded there."
        ),
    },
    "Transformation of Tzeentch": {
        "CN": 12,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "At your command, bonds of aethyric fire coil from the earth, shrouding"
            " your target in a cocoon of magical energy. The target gains the Prone"
            " Condition and is considered Helpless for the duration. At the end of each"
            " Round, they must pass a Challenging (+0 SL) Endurance Test or gain 1"
            " Corruption Point."
        ),
    },
    "Treason of Tzeentch": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "AoE (Initiative Bonus yards)",
        "duration": "Intelligence Bonus Rounds",
        "description": (
            "You channel fine strands of traitorous thoughts into your targets’ minds,"
            " twisting their motivations and fanning fires of discontent. Targets gain"
            " Animosity (Allies). Further, unless immune to that Psychology, they"
            " cannot transfer Advantage to their allies and, if they score a Critical"
            " when attacking, they must pass a Hard (-2 SL) Cool Test or target their"
            " nearest ally."
        ),
    },
}
