import pytest
import pygame
from player import Player

knockback_detail = [
    (10,'left',1),
    (10,'right',1)
]

@pytest.mark.parametrize("strength_y, direction, ratio", knockback_detail)
def test_knockback(strength_y, direction, ratio):
    """
    """
    Player().knockback(strength_y, direction, ratio)
    assert Player().vel == vec(strength_y, strength_y)
