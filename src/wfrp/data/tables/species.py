SPECIES = {
    90: "Human",
    94: "Halfling",
    98: "Dwarf",
    99: "High Elf",
    00: "Wood Elf",
}


def get_species(die_roll):
    if die_roll < 90:
        die_roll = 90
    while True:
        try:
            return SPECIES[die_roll]
        except KeyError:
            die_roll += 1
