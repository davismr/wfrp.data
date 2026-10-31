from wfrp.data.dice import roll_d10


def get_class_trappings(career_class):
    trappings = ["Clothing", "Dagger", "Pouch"]
    if career_class == "Academics":
        trappings.append(
            f"Sling Bag containing Writing Kit and {roll_d10()} sheets of Parchment",
        )
    elif career_class == "Burghers":
        trappings.extend([
            "Cloak",
            "Hat",
            "Sling Bag containing Lunch",
        ])
    elif career_class == "Courtiers":
        trappings.extend(["Fine Clothing", "Tweezers", "Ear Pick", "Comb"])
    elif career_class == "Peasants":
        trappings.extend([
            "Cloak",
            "Sling Bag containing Rations (1 day)",
        ])
    elif career_class == "Rangers":
        trappings.extend([
            "Cloak",
            "Backpack containing Tinderbox",
            "Blanket",
            "Rations (1 day)",
        ])
    elif career_class == "Riverfolk":
        trappings.extend([
            "Cloak",
            "Sling Bag containing a Flask of Spirits",
        ])
    elif career_class == "Rogues":
        trappings.extend([
            "Sling Bag containing 2 Candles",
            f"{roll_d10()} Matches",
            "Hood or Mask",
        ])
    elif career_class == "Warriors":
        trappings.append("Hand Weapon")
    else:
        raise NotImplementedError("Career class not defined")
    return trappings
