from random import randint


def roll_d10(modifier=0):
    return randint(1, 10) + modifier


def roll_2d10(modifier=0):
    return roll_d10() + roll_d10() + modifier


def roll_3d10(modifier=0):
    return roll_d10() + roll_d10() + roll_d10() + modifier


def roll_5d10(modifier=0):
    return roll_2d10() + roll_3d10() + modifier


def roll_8d10(modifier=0):
    return roll_4d10() + roll_4d10() + modifier


def roll_10d10(modifier=0):
    return roll_5d10() + roll_5d10() + modifier


def roll_d100(modifier=0):
    tens_die = roll_d10(-1) * 10
    return tens_die + roll_d10() + modifier
