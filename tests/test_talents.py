from wfrp.data.tables.talents import TALENT_LIST
from wfrp.data.tables.talents import get_random_talent
from wfrp.data.talents import TALENT_DATA


def test_talent_descriptions():
    for talent in TALENT_DATA:
        assert TALENT_DATA[talent]["description"], talent


def test_random_talents():
    for talent in TALENT_LIST.values():
        assert talent.split(" (")[0] in TALENT_DATA


def test_get_talent():
    talent = get_random_talent(61)
    assert talent == "Resistant (Poison)"
