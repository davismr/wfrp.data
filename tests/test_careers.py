import pytest

from wfrp.data.careers.academics import ACADEMIC_CLASS
from wfrp.data.careers.burghers import BURGHERS_CLASS
from wfrp.data.careers.courtiers import COURTIERS_CLASS
from wfrp.data.careers.peasants import PEASANTS_CLASS
from wfrp.data.careers.rangers import RANGERS_CLASS
from wfrp.data.careers.riverfolk import RIVERFOLK_CLASS
from wfrp.data.careers.rogues import ROGUES_CLASS
from wfrp.data.careers.warriors import WARRIORS_CLASS
from wfrp.data.constants import Characteristics
from wfrp.data.skills import SKILL_DATA
from wfrp.data.tables.careers import get_career
from wfrp.data.tables.careers import list_careers
from wfrp.data.talents import TALENT_DATA


def assert_career_level(career, career_name, career_level, level):  # noqa: C901
    assert career, career_name
    for key, item in career_level.items():
        if key == "status":
            assert list(item.keys()) == ["tier", "standing"]
            assert item["tier"] in ["Gold", "Silver", "Brass"]
            assert isinstance(item["standing"], int)
            if career_name == "Flagellant" or career == "Pauper":
                assert item["standing"] == 0
            else:
                assert item["standing"] > 0
        elif key == "characteristics":
            if level == 1:
                assert len(item) == 3
            else:
                assert len(item) == 1
            for characteristic in item:
                assert characteristic in Characteristics
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
        WARRIORS_CLASS,
    ],
)
def test_basic_career_data(career_data):
    # 8 careers per class
    assert len(career_data) == 8
    for career, career_class in career_data.items():
        # should be 4 career levels plus income
        assert len(career_class) == 5
        for level, (career_level, career_data) in enumerate(career_class.items()):
            if career_level == "income":
                assert isinstance(career_level, str)
                continue
            assert_career_level(career_level, career, career_data, level)


@pytest.mark.parametrize(
    "species, career",
    [
        ("Human", "Hunter"),
        ("Dwarf", "Servant"),
        ("Halfling", "Servant"),
        ("High Elf", "Spy"),
        ("Wood Elf", "Herbalist"),
    ],
)
def test_get_career(species, career):
    random_career = get_career(species, 42)
    assert random_career == career


def test_get_career_invalid():
    with pytest.raises(NotImplementedError):
        get_career("Not a species", 42)


def test_not_integer():
    with pytest.raises(TypeError):
        get_career("Human", "Not a number")


def test_list_careers():
    careers = list_careers()
    assert len(careers) == 64


def test_list_human_careers():
    careers = list_careers("Human")
    assert len(careers) == 63
    assert "Slayer" not in careers


def test_list_dwarf_careers():
    careers = list_careers("Dwarf")
    assert len(careers) == 47
    assert "Slayer" in careers
    assert "Knight" not in careers


def test_list_halfling_careers():
    careers = list_careers("Halfling")
    assert len(careers) == 48
    assert "Slayer" not in careers
    assert "Road Warden" in careers


def test_list_high_elf_careers():
    careers = list_careers("High Elf")
    assert len(careers) == 36
    assert "Slayer" not in careers
    assert "Knight" in careers
    assert "Smuggler" in careers


def test_list_wood_elf_careers():
    careers = list_careers("Wood Elf")
    assert len(careers) == 22
    assert "Slayer" not in careers
    assert "Wrecker" in careers


def test_list_careers_invalid():
    with pytest.raises(NotImplementedError):
        list_careers("Not a species")
