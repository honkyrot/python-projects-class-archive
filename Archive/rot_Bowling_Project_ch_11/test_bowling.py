import Saving_Bowling_v3
import pytest


@pytest.fixture()
def bowling():
    """Start a bowling game!"""
    return Saving_Bowling_v3.BowlingGame()


def test_score_1(bowling):
    """Test scoring, all strikes."""
    bowling.hit_count = [[1, [10, 10]], [2, [10, 10]], [3, [10, 10]], [4, [10, 10]], [5, [10, 10]], [6, [10, 10]], [7, [10, 10]], [8, [10, 10]], [9, [10, 10]], [10, [10, 10, 10]]]
    assert "| _ X | _ X | _ X | _ X | _ X | _ X | _ X | _ X | _ X | X X X |" == bowling.human_readable_format()
