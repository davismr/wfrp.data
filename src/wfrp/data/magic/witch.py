LORE_HEDGECRAFT = {
    "Goodwill": {
        "CN": 0,
        "range": "You",
        "target": "AoE (Fellowship Bonus yards)",
        "duration": "Willpower Bonus minutes",
        "description": (
            "You create an atmosphere conducive to friendliness and good spirits. All"
            " Fellowship Tests within the Area of Effect receive +1 SL, and Animosity"
            " and Hatred Psychologies have no effect."
        ),
    },
    "Halétha’s Joy": {
        "CN": 0,
        "range": "Touch",
        "target": 1,
        "duration": "Fellowship Bonus hours",
        "description": (
            "You plead with a god of fertility to bless the target. While the Spell is"
            " active, if biologically possible, they will conceive a child. The Spell"
            " ends when used."
        ),
    },
    "Mirkride": {
        "CN": 0,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus minutes",
        "description": [
            (
                "Speaking ancient words of magic, your spirit leaves your body,"
                " stepping into the Hedge, the dark space between the material world"
                " and the spirit realm. For the duration, you stand apart from the"
                " world, able to witness it invisibly and completely silently, but not"
                " affect it in any way. Your spirit self has the Ethereal Trait (see"
                " page 358). Your body remains in place, immobile and insensate."
            ),
            (
                "If you take any Magical damage, it instead immediately ends the Spell."
                " You can see and interact with spirits, other Ethereal creatures, and"
                " daemons, even invisible ones, and vice versa."
            ),
            (
                "At the end of the Spell, you are pulled suddenly back to your body. If"
                " your body is killed while you are walking the Hedge, your spirit will"
                " wander aimlessly for eternity."
            ),
        ],
    },
    "Nepenthe": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower Bonus hours",
        "description": (
            "As you chant your incantations over a cup, a thick mist issues from your"
            " mouth and coalesces as a thick, silver liquid. A character who drinks it"
            " within the duration may choose to completely forget one individual,"
            " permanently."
        ),
    },
    "Nostrum": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Dexterity Bonus hours",
        "description": (
            "You incant a spell over a prepared draught, imbuing it with magical power."
            " If drunk while the Spell is active, the drinker immediately heals"
            " Dexterity Bonus Wounds and is cured of one disease of the GM’s choice."
            " For every +2 SL, you may cure an extra disease."
        ),
    },
    "Part the Branches": {
        "CN": 0,
        "range": "You",
        "target": "You",
        "duration": "Initiative minutes",
        "description": (
            "Your pupils dilate as you complete your incantation, allowing you to see"
            " into the spirit world. This allows you to see all invisible creatures."
        ),
    },
    "Protective Charm": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower Bonus days",
        "description": (
            "You imbue a charm, such as a small piece of jewellery or pocket-sized"
            " trinket, with a spell of protection. Those bearing the charm gain +2 SL"
            " to resist magical effects and Corruption."
        ),
    },
    "Shepherd’s Eye": {
        "CN": 0,
        "range": "Special",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "This spell is most often used to find lost livestock, but is easily put to"
            " other uses. You grab a bit of organic matter belonging to a single"
            " creature — wool, blood, a piece of their leavings — and add it to a bowl"
            " of water. After scrying into the bowl for 10 - IB minutes, secret symbols"
            " appear to your sight: the GM will describe the creature’s location. If"
            " you are familiar with the location, you know where they are."
        ),
    },
}

LORE_WITCHCRAFT = {
    "Blight": {
        "CN": 14,
        "range": "Willpower Bonus yards",
        "target": "Special",
        "duration": "Instant",
        "description": [
            (
                "You cause an area to become blighted or desolate. For example you may"
                " target either a tavern, well, field, or a domestic animal. If you"
                " successfully cast the Spell, the target suffers from a blight:"
            ),
            "All food and drink in a blighted tavern immediately spoils.",
            "A blighted well becomes instantly brackish and stagnant.",
            "Any crops currently planted in a blighted field rot overnight.",
            (
                "A blighted animal sickens. The afflicted beast no longer produces"
                " anything (cows produce no milk, coats and hides grow mangy and"
                " unusable) and will die in 24 - SL days."
            ),
        ],
    },
    "Creeping Menace": {
        "CN": 6,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You summon a swarm of creeping, slithering creatures to harass your foes."
            " Each target affected is immediately Engaged by a swarm of Giant Rats,"
            " Giant Spiders, or similar (your choice of one creature type). Use the"
            " standard profiles for the relevant creature type, adding the Swarm Trait."
            " For your Action, you may make a Challenging (+0 SL) Charm Animal Test to"
            " direct one or more swarms to attack a different target. When the Spell"
            " ends, any remaining swarms disappear into the shadows."
        ),
    },
    "Curse of Crippling Pain": {
        "CN": 10,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": [
            (
                "Stabbing a crude representation of your target — a doll or puppet —"
                " you inflict crippling pain. When successfully cast, choose which Hit"
                " Location to stab:"
            ),
            (
                "Body — Target doubles up in agony, gaining +1 Fatigued, and must pass"
                " a Hard (-2 SL) Endurance Test or fall Prone."
            ),
            (
                "Head — Target gains a Stunned Condition, and must pass an Average (+2"
                " SL) Endurance Test or gain -SL additional Stunned."
            ),
            "Limb — Limb becomes useless, as if amputated (see page 177).",
            (
                "Fatigued and Stunned last for the duration. You may stab the doll"
                " again to affect an additional, unaffected Location by using an Action"
                " to take an Average (+2 SL) Channelling Test."
            ),
        ],
    },
    "Curse of Ill Fortune": {
        "CN": 8,
        "range": "Willpower yards or Willpower Bonus miles (with ingredient)",
        "target": 1,
        "duration": "Willpower Bonus minutes or days (with ingredient)",
        "description": (
            "The target suffers bad luck. Laces snap, chairs break, and other minor"
            " narrative effects inconvenience them. They suffer -1 SL to all Tests and"
            " cannot spend Fortune. If they have no Fortune, they reroll all Test rolls"
            " of 01–05. This Spell’s ingredient, something belonging to the target"
            " (such as a personal possession or strand of hair), lets you ignore line"
            " of sight."
        ),
    },
    "Glamour": {
        "CN": 4,
        "range": "Touch",
        "target": "1 adult",
        "duration": "Willpower Bonus hours",
        "description": (
            "You alter the target’s appearance to look however old you wish, within the"
            " normal range of adulthood."
        ),
    },
    "Haunting Horror": {
        "CN": 8,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower days",
        "description": (
            "You target a single location, such as a house or clearing, and inflict"
            " haunting dreams and waking nightmares on any who enter there. Those"
            " entering while the Spell is active are unnerved by eerie sensations,"
            " flitting shadows, and whispered voices lurking on the threshold of"
            " hearing. Unless they are witches or their familiars, they gain +1"
            " Fatigued Condition. Then, unless they pass a Challenging (+0 SL)"
            " Psychology Test, they gain another Fatigued Condition and a Broken"
            " Condition, both of which are only removed upon leaving the location."
        ),
    },
    "Make Hale": {
        "CN": 4,
        "range": "Touch",
        "target": 1,
        "duration": "Instant",
        "description": (
            "Your hands glow with a soothing, pale yellow light and the target relaxes."
            " They heal WPB Wounds and lose 1 Fatigued and 1 Stunned. With +3 SL, you"
            " may change Range to Willpower Bonus yards, causing streams of light to"
            " leap from your fingers and twist through the air."
        ),
    },
    "The Evil Eye": {
        "CN": 6,
        "range": "10 yards (maximum)",
        "target": "1 (maximum)",
        "duration": "Instant",
        "description": (
            "You lock eyes with the target and wither their psyche. Perform an Opposed"
            " Intimidate/Cool Test, adding any SL from the Casting Test to your result."
            " If you win, the target suffers Fear 1 from you and gains 1 Fatigued"
            " Condition, plus 1 Fatigued per +3 SL by which you win. If you win by 6+"
            " SL, they gain 1 Broken Condition."
        ),
    },
}
