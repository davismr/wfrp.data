from wfrp.data.constants import Attributes

RIVERFOLK_CLASS = {
    "Boatman": {
        "income": "Sail",
        "Boathand": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": [Attributes.S, Attributes.T, Attributes.Ag],
            "skills": [
                "Athletics",
                "Charm",
                "Consume Alcohol",
                "Dodge",
                "Endurance",
                "Gossip",
                "Melee (Brawling)",
                "Row",
                "Sail",
                "Swim",
            ],
            "talents": [
                "Fisherman",
                "Strong Back",
                "Strong Swimmer",
                "Waterman",
            ],
            "trappings": [
                "Hand Weapon (Boat Hook)",
                "Leather Jack",
                "Pole",
            ],
        },
        "Boatman": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": [Attributes.I],
            "skills": [
                "Entertain (Storytelling)",
                "Haggle",
                "Navigation",
                "Lore (Riverways)",
                "Perception",
                "Secret Signs (Guilder)",
            ],
            "talents": [
                "Dirty Fighting",
                "Etiquette (Guilder)",
                "Seasoned Traveller",
                "Very Strong",
            ],
            "trappings": [
                "Rope",
                "Rowboat",
            ],
        },
        "Bargeswain": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": [Attributes.Dex],
            "skills": [
                "Climb",
                "Heal",
                "Intuition",
                "Trade (Boatbuilder)",
            ],
            "talents": [
                "Craftsman (Boatbuilder)",
                "Dealmaker",
                "Embezzle",
                "Nose for Trouble",
            ],
            "trappings": [
                "Backpack",
                "Trade Tools (Carpenter)",
                "Trade Tools (Physician)",
            ],
        },
        "Barge Master": {
            "status": {"tier": "Silver", "standing": 5},
            "attributes": [Attributes.Int],
            "skills": [
                "Cool",
                "Leadership",
            ],
            "talents": [
                "Orientation",
                "Pilot",
                "Public Speaker",
                "Savant (Riverways)",
            ],
            "trappings": [
                "Barge and Crew",
                "Hat",
            ],
        },
    },
}
