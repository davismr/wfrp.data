from wfrp.data.constants import Attributes

ACADEMIC_CLASS = {
    "Apothecary": {
        "income": "Trade (Apothecary)",
        "Apothecary’s Apprentice": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": [Attributes.I, Attributes.Dex, Attributes.Int],
            "skills": [
                "Consume Alcohol",
                "Endurance",
                "Haggle",
                "Heal",
                "Language (Classical)",
                "Lore (Chemistry)",
                "Lore (Medicine)",
                "Perception",
                "Trade (Apothecary)",
                "Trade (Poisoner)",
            ],
            "talents": [
                "Acute Sense (Taste)",
                "Concoct",
                "Craftsman (Apothecary)",
                "Read/Write",
            ],
            "trappings": [
                "Book (Blank)",
                "Leather Jerkin",
                "Pestle and Mortar",
            ],
        },
        "Apothecary": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": [Attributes.Fel],
            "skills": [
                "Charm",
                "Evaluate",
                "Gossip",
                "Language (Guilder)",
                "Secret Signs (Guilder)",
                "Stealth (Urban)",
            ],
            "talents": [
                "Criminal",
                "Dealmaker",
                "Etiquette (Guilder)",
                "Pharmacist",
            ],
            "trappings": [
                "Guild Licence",
                "Trade Tools (Apothecary)",
            ],
        },
        "Master Apothecary": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": [Attributes.T],
            "skills": [
                "Intuition",
                "Leadership",
                "Lore (Science)",
                "Research",
            ],
            "talents": [
                "Bookish",
                "Etiquette (Criminals or Scholars)",
                "Master Tradesman (Apothecary)",
                "Resistant (Poison)",
            ],
            "trappings": [
                "Apprentice",
                "Book (Apothecary)",
                "Workshop (Apothecary)",
            ],
        },
        "Apothecary-General ": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": [Attributes.WP],
            "skills": [
                "Bribery",
                "Intimidate",
            ],
            "talents": [
                "Coolheaded",
                "Kingpin",
                "Savant (Chemistry)",
                "Savvy",
            ],
            "trappings": [
                "Commission Papers",
                "Large Workshop (Apothecary)",
            ],
        },
    },
    "Engineer": {
        "income": "Trade (Engineer)",
        "Student Engineer": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": [Attributes.S, Attributes.Dex, Attributes.Int],
            "skills": [
                "Art (Drawing)",
                "Consume Alcohol",
                "Cool",
                "Endurance",
                "Evaluate",
                "Language (Classical)",
                "Lore (Engineering)",
                "Ranged (Engineering)",
                "Research",
                "Trade (Engineer)",
            ],
            "talents": [
                "Craftsman (Engineer)",
                "Read/Write",
                "Tinker",
                "Unshakeable",
            ],
            "trappings": [
                "Book (Engineer)",
                "Hammer and Spikes",
            ],
        },
        "Engineer": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": [Attributes.BS],
            "skills": [
                "Drive",
                "Language (Guilder)",
                "Lore (Science)",
                "Navigation",
                "Ride (Horse)",
                "Secret Signs (Guilder)",
            ],
            "talents": [
                "Etiquette (Guilder)",
                "Etiquette (Scholars)",
                "Gunner",
                "Marksman",
            ],
            "trappings": [
                "Guild Licence",
                "Trade Tools (Engineer)",
            ],
        },
        "Master Engineer ": {
            "status": {"tier": "Silver", "standing": 5},
            "attributes": [Attributes.I],
            "skills": [
                "Animal Training (Pigeon)",
                "Dodge",
                "Language (Khazalid)",
                "Leadership",
            ],
            "talents": [
                "Master Tradesman (Engineer)",
                "Orientation",
                "Sniper",
                "Super Numerate",
            ],
            "trappings": [
                "Workshop (Engineer)",
            ],
        },
        "Chartered Engineer": {
            "status": {"tier": "Gold", "standing": 2},
            "attributes": [Attributes.WP],
            "skills": [
                "Language (Any One)",
                "Perception",
            ],
            "talents": [
                "Embezzle",
                "Magnum Opus",
                "Rapid Reload",
                "Savant (Engineering)",
            ],
            "trappings": [
                "Library (Engineering)",
                "Quality Trade Tools (Engineer)",
                "Large Workshop (Engineer)",
            ],
        },
    },
    "Lawyer": {
        "income": "Lore (Law)",
        "Student Lawyer": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": [Attributes.I, Attributes.Int, Attributes.Fel],
            "skills": [
                "Bribery",
                "Charm",
                "Consume Alcohol",
                "Entertain (Storytelling)",
                "Gossip",
                "Intuition",
                "Language (Classical)",
                "Lore (Law)",
                "Lore (Theology)",
                "Research",
            ],
            "talents": [
                "Blather",
                "Etiquette (Scholars)",
                "Read/Write",
                "Speedreader",
            ],
            "trappings": [
                "Book (Law)",
                "Magnifying Glass",
            ],
        },
        "Lawyer": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": [Attributes.WP],
            "skills": [
                "Cool",
                "Haggle",
                "Intimidate",
                "Language (Guilder)",
                "Lore (Local)",
                "Secret Signs (Guilder)",
            ],
            "talents": [
                "Argumentative",
                "Briber",
                "Etiquette (Criminals)",
                "Etiquette (Guilder)",
            ],
            "trappings": [
                "Court Robes",
                "Guild Licence",
                "Writing Kit",
            ],
        },
        "Barrister": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": [Attributes.Dex],
            "skills": [
                "Art (Writing)",
                "Entertain (Speeches)",
                "Lore (Politics)",
                "Perception",
            ],
            "talents": [
                "Cat-tongued",
                "Impassioned Zeal",
                "Menacing",
                "Savant (Law)",
            ],
            "trappings": [
                "Assistant (Student or Servant)",
                "Office",
            ],
        },
        "Judge": {
            "status": {"tier": "Gold", "standing": 2},
            "attributes": [Attributes.T],
            "skills": [
                "Leadership",
                "Lore (Any One)",
            ],
            "talents": [
                "Bookish",
                "Commanding Presence",
                "Master Orator",
                "Savvy",
            ],
            "trappings": [
                "Gavel",
                "Ostentatious Wig",
            ],
        },
    },
    "Nun": {
        "income": "Lore (Theology)",
        "Novice": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": [Attributes.Dex, Attributes.Int, Attributes.Fel],
            "skills": [
                "Art (Calligraphy)",
                "Charm",
                "Cool",
                "Endurance",
                "Heal",
                "Language (Classical)",
                "Lore (Theology)",
                "Outdoor Survival",
                "Pray",
                "Trade (Brewer)",
            ],
            "talents": [
                "Bless (Any One)",
                "Holy Visions",
                "Panhandle",
                "Read/Write",
            ],
            "trappings": [
                "Religious Symbol",
                "Robes",
            ],
        },
        "Nun": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": [Attributes.WP],
            "skills": [
                "Entertain (Storytelling)",
                "Gossip",
                "Intuition",
                "Language (Any One)",
                "Lore (Local)",
                "Melee (Any One)",
            ],
            "talents": [
                "Etiquette (Cultists)",
                "Field Dressing",
                "Invoke (Any One)",
                "Seasoned Traveller",
            ],
            "trappings": [
                "Book (Religion)",
                "Religious Relic",
            ],
        },
        "Abbess": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": [Attributes.T],
            "skills": [
                "Intimidate",
                "Leadership",
                "Lore (Politics)",
                "Perception",
            ],
            "talents": [
                "Inspiring",
                "Resistant (Any One)",
                "Savant (Theology)",
                "Stout-hearted",
            ],
            "trappings": [
                "Abbey",
                "Library (Theology)",
            ],
        },
        "Prioress General ": {
            "status": {"tier": "Gold", "standing": 4},
            "attributes": [Attributes.I],
            "skills": [
                "Lore (Any One)",
                "Research",
            ],
            "talents": [
                "Commanding Presence",
                "Iron Will",
                "Pure Soul",
                "Strong-minded",
            ],
            "trappings": [
                "Religious Order",
            ],
        },
    },
}
