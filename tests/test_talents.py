from wfrp.data.careers.data import CAREER_DATA
from wfrp.data.tables.talents import TALENT_LIST
from wfrp.data.tables.talents import get_random_talent
from wfrp.data.talents import TALENT_DATA


def test_talents():
    missing = []
    for career_data in CAREER_DATA:
        for career in CAREER_DATA[career_data]:
            if career == "income":
                continue
            for talent in CAREER_DATA[career_data][career]["talents"]:
                talent = talent.split(" (")[0]
                if talent not in TALENT_DATA:
                    missing.append(talent)
    assert not missing, sorted(missing)


def test_talent_descriptions():
    for talent in TALENT_DATA:
        assert TALENT_DATA[talent]["description"], talent


def test_random_talents():
    for talent in TALENT_LIST.values():
        assert talent.split(" (")[0] in TALENT_DATA


def test_get_talent():
    talent = get_random_talent(61)
    assert talent == "Resistant (Poison)"
