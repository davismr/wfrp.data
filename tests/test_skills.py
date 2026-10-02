from wfrp.data.constants import Attributes
from wfrp.data.skills import SKILL_DATA


def test_skill_characteristics():
    for skill in SKILL_DATA:
        assert SKILL_DATA[skill]["characteristic"] in Attributes._member_map_
