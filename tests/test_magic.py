import pytest

from wfrp.data.magic.aqshy import LORE_FIRE
from wfrp.data.magic.azyr import LORE_BEASTS
from wfrp.data.magic.chamon import LORE_METAL
from wfrp.data.magic.ghar import LORE_HEAVENS
from wfrp.data.magic.ghyran import LORE_LIFE
from wfrp.data.magic.hysh import LORE_LIGHT
from wfrp.data.magic.shyish import LORE_DEATH
from wfrp.data.magic.ulgu import LORE_SHADOWS


@pytest.mark.parametrize(
    "lore_data",
    [
        LORE_FIRE,
        LORE_BEASTS,
        LORE_METAL,
        LORE_HEAVENS,
        LORE_LIFE,
        LORE_LIGHT,
        LORE_DEATH,
        LORE_SHADOWS,
    ],
)
def test_lores(lore_data):
    assert len(lore_data) == 8
    for lore in lore_data:
        spell = lore_data[lore]
        assert spell["CN"] > 0
        assert isinstance(spell["description"], (str, list))
        assert isinstance(spell["range"], str)
        assert isinstance(spell["duration"], str)
        assert "target" in spell
