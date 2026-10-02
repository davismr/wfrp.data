from wfrp.data.talents import TALENT_DATA


def test_talent_descriptions():
    for talent in TALENT_DATA:
        assert TALENT_DATA[talent]["description"], talent
