import pytest
import pygame as pg
from controller import KeyboardController
from controller import KeyboardController2
test_player = Player()

# keystrokes1_detail = [
#     (pg.event.Event(pg.KEYDOWN, key=pg.K_LEFT), ),
#     (pg.event.Event(pg.KEYDOWN, key=pg.K_RIGHT), ),
#     (pg.event.Event(pg.KEYDOWN, key=pg.K_SPACE), 0),
#     (pg.event.Event(pg.KEYDOWN, key=pg.K_UP), 0),
#     (pg.event.Event(pg.KEYDOWN, key=pg.K_SLASH), )
# ]
jump1_detail = [
    (pg.event.Event(pg.KEYDOWN, key=pg.K_SPACE), 0 ),
    (pg.event.Event(pg.KEYDOWN, key=pg.K_UP), 0)
]

@pytest.mark.parametrize("event, jump_count", jump1_detail)
def test_knockback(event, jump_count):
    """
    """
    pg.event.post(event)
    assert KeyboardController.move().player.Player().jump_count == 1
