import pytest

from wfrp.data.careers.academics import ACADEMIC_CLASS
from wfrp.data.careers.burghers import BURGHERS_CLASS
from wfrp.data.careers.courtiers import COURTIERS_CLASS

# from wfrp.character.data.careers.deft_steps import DEFT_STEPS_CLASS_DATA
# from wfrp.character.data.careers.high_elf import HIGH_ELF_CLASS_DATA
from wfrp.data.careers.peasants import PEASANTS_CLASS
from wfrp.data.careers.rangers import RANGERS_CLASS
from wfrp.data.careers.riverfolk import RIVERFOLK_CLASS
from wfrp.data.careers.rogues import ROGUES_CLASS

# from wfrp.character.data.careers.seafarer import PRIEST_OF_STROMFELS
# from wfrp.character.data.careers.seafarer import SEAFARER_CLASS_DATA
# from wfrp.character.data.careers.tables import get_career
# from wfrp.character.data.careers.tables import list_careers
# from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CLASS_DATA
from wfrp.data.careers.warriors import WARRIORS_CLASS
from wfrp.data.constants import Attributes

# from wfrp.character.data.careers.winds_of_magic import WINDS_OF_MAGIC_CLASS_DATA
from wfrp.data.skills import SKILL_DATA
from wfrp.data.talents import TALENT_DATA


def assert_career_level(career, career_name, career_level, level):  # noqa: C901
    for key, item in career_level.items():
        if key == "status":
            assert list(item.keys()) == ["tier", "standing"]
            assert item["tier"] in ["Gold", "Silver", "Brass"]
            assert isinstance(item["standing"], int)
            if career_name == "Flagellant" or career == "Pauper":
                assert item["standing"] == 0
            else:
                assert item["standing"] > 0
        elif key == "attributes":
            if level == 1:
                assert len(item) == 3
            else:
                assert len(item) == 1
            for attribute in item:
                assert attribute in Attributes
        elif key == "skills":
            if level == 1:
                assert len(item) in [8, 10]
            elif level == 2:
                if career_name in ["Freelance", "Knight of the Blazing Sun"]:
                    assert len(item) == 7
                else:
                    assert len(item) == 6
            elif level == 3:
                assert len(item) == 4
            elif level == 4:
                assert len(item) == 2
            for skill_string in item:
                skill_string = skill_string.split(" (")[0]
                for skill in skill_string.split(" or "):
                    assert skill in SKILL_DATA
        elif key == "talents":
            assert len(item) == 4
            for talent in item:
                assert talent.split(" (")[0] in TALENT_DATA, talent
        elif key == "trappings":
            # TODO test trappings
            assert True
        else:
            assert False, f"Unexpected Key {key}"


@pytest.mark.parametrize(
    "career_data",
    [
        ACADEMIC_CLASS,
        BURGHERS_CLASS,
        COURTIERS_CLASS,
        PEASANTS_CLASS,
        RANGERS_CLASS,
        RIVERFOLK_CLASS,
        ROGUES_CLASS,
        # SEAFARER_CLASS_DATA,
        WARRIORS_CLASS,
    ],
)
def test_basic_career_data(career_data):
    # 8 careers per class
    # assert len(career_data) == 8
    for career, career_class in career_data.items():
        # should be 4 career levels plus income
        assert len(career_class) == 5
        for level, (career_level, career_data) in enumerate(career_class.items()):
            if career_level == "income":
                assert isinstance(career_level, str)
                continue
            assert_career_level(career_level, career, career_data, level)


# @pytest.mark.parametrize(
#     "career_data",
#     [
#         DEFT_STEPS_CLASS_DATA,
#         HIGH_ELF_CLASS_DATA,
#         PRIEST_OF_STROMFELS,
#         UP_IN_ARMS_CLASS_DATA,
#         WINDS_OF_MAGIC_CLASS_DATA,
#     ],
# )
# def test_career_data(career_data):
#     for career_name, career_class in career_data.items():
#         # should be 4 career levels
#         assert len(career_class) == 4
#         level = 1
#         for career, career_level in career_class.items():
#             assert career, f"Missing career title in {list(career_class.keys())[1]}"
#             assert_career_level(career, career_name, career_level, level)
#             level += 1
