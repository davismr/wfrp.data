from wfrp.data.careers.data import CAREER_DATA
from wfrp.data.constants import Characteristics
from wfrp.data.skills import SKILL_DATA


def test_skill_characteristics():
    for skill in SKILL_DATA:
        assert SKILL_DATA[skill]["characteristic"] in Characteristics


def test_skill():
    missing = []
    for career_data in CAREER_DATA:
        for career in CAREER_DATA[career_data]:
            if career == "income":
                continue
            for skill in CAREER_DATA[career_data][career]["skills"]:
                skill = skill.split(" (")[0]
                if " or " in skill:
                    for skill in skill.split(" or "):
                        if skill not in SKILL_DATA:
                            missing.append(skill)
                else:
                    if skill not in SKILL_DATA:
                        missing.append(skill)
    assert not missing, sorted(missing)
