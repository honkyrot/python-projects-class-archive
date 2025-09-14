"""Does testing for bowling, mainly scoring adjustments."""

import pytest
import bowling_core


@pytest.fixture()
def bowling_v2():
    """Provides BOWLING"""
    return bowling_core.BowlingGame()


def test_check_score_1_all_strikes(bowling_v2):
    """Test scoring calculations and reading. Test 1: All strikes"""
    bowling_v2.scoreboard = {1: [10], 2: [10], 3: [10], 4: [10], 5: [10],
                             6: [10], 7: [10], 8: [10], 9: [10], 10: [10, 10, 10]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 300
    assert bowling_v2.readable_scoreboard() == "| _ X | _ X | _ X | _ X | _ X | _ X | _ X | _ X | _ X | X X X |"


def test_check_score_2_all_spares(bowling_v2):
    """Test scoring calculations and reading. Test 2: All spares"""
    bowling_v2.scoreboard = {1: [5, 5], 2: [5, 5], 3: [5, 5], 4: [5, 5], 5: [5, 5],
                             6: [5, 5], 7: [5, 5], 8: [5, 5], 9: [5, 5], 10: [5, 5, 5]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 150
    assert bowling_v2.readable_scoreboard() == "| 5 / | 5 / | 5 / | 5 / | 5 / | 5 / | 5 / | 5 / | 5 / | 5 / 5 |"


def test_check_score_3_alt_strikes(bowling_v2):
    """Test scoring calculations and reading. Test 3: Alternating Strikes"""
    bowling_v2.scoreboard = {1: [10], 2: [0, 0], 3: [10], 4: [0, 0], 5: [10],
                             6: [0, 0], 7: [10], 8: [0, 0], 9: [10], 10: [0, 0]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 50
    assert bowling_v2.readable_scoreboard() == "| _ X | 0 0 | _ X | 0 0 | _ X | 0 0 | _ X | 0 0 | _ X | 0 0 "


def test_check_score_4_alt_spares(bowling_v2):
    """Test scoring calculations and reading. Test 4: Alternating Spares"""
    bowling_v2.scoreboard = {1: [5, 5], 2: [0, 0], 3: [5, 5], 4: [0, 0], 5: [5, 5],
                             6: [0, 0], 7: [5, 5], 8: [0, 0], 9: [5, 5], 10: [0, 0]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 50
    assert bowling_v2.readable_scoreboard() == "| 5 / | 0 0 | 5 / | 0 0 | 5 / | 0 0 | 5 / | 0 0 | 5 / | 0 0 "


def test_check_score_5_random_set_1(bowling_v2):
    """Test scoring calculations and reading. Test 5: Random Set 1"""
    bowling_v2.scoreboard = {1: [9, 0], 2: [2, 4], 3: [10], 4: [8, 0], 5: [9, 1],
                             6: [10], 7: [1, 3], 8: [2, 8], 9: [10], 10: [0, 4]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 117
    assert bowling_v2.readable_scoreboard() == "| 9 0 | 2 4 | _ X | 8 0 | 9 / | _ X | 1 3 | 2 / | _ X | 0 4 "


def test_check_score_6_random_set_2(bowling_v2):
    """Test scoring calculations and reading. Test 6: Random Set 2"""
    bowling_v2.scoreboard = {1: [10], 2: [5, 2], 3: [8, 2], 4: [1, 6], 5: [9, 1],
                             6: [8, 0], 7: [10], 8: [2, 3], 9: [10], 10: [5, 5, 9]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 127
    assert bowling_v2.readable_scoreboard() == "| _ X | 5 2 | 8 / | 1 6 | 9 / | 8 0 | _ X | 2 3 | _ X | 5 / 9 |"


def test_check_score_7_random_set_3(bowling_v2):
    """Test scoring calculations and reading. Test 7: Random Set 3"""
    bowling_v2.scoreboard = {1: [2, 7], 2: [0, 8], 3: [7, 1], 4: [1, 9], 5: [6, 2],
                             6: [10], 7: [3, 1], 8: [1, 9], 9: [9, 0], 10: [10, 10, 4]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 119
    assert bowling_v2.readable_scoreboard() == "| 2 7 | 0 8 | 7 1 | 1 / | 6 2 | _ X | 3 1 | 1 / | 9 0 | X X 4 |"


def test_check_score_8_random_set_4(bowling_v2):
    """Test scoring calculations and reading. Test 8: Random Set 4"""
    bowling_v2.scoreboard = {1: [1, 9], 2: [9, 0], 3: [1, 4], 4: [7, 0], 5: [5, 0],
                             6: [5, 1], 7: [8, 1], 8: [2, 7], 9: [10], 10: [10, 8, 2]}
    bowling_v2.calculate_score()
    assert bowling_v2.score == 117
    assert bowling_v2.readable_scoreboard() == "| 1 / | 9 0 | 1 4 | 7 0 | 5 0 | 5 1 | 8 1 | 2 7 | _ X | X 8 / |"


def test_check_score_9_fail_random_set(bowling_v2):
    """Test fail condition if scoreboard is somehow invalid. Strike Version."""
    bowling_v2.scoreboard = {1: [2, 7], 2: [0, 8], 3: [7, 1], 4: [1, 9], 5: [6, 2],
                             6: [10], 7: [3, 1], 8: [1, 9], 9: [9, 0], 10: [10, 10]}
    assert bowling_v2.calculate_score() == "MISSING 3RD VALUE FOR 10th STRIKE"


def test_reset_frame(bowling_v2):
    """Basic test for confirming reset."""
    bowling_v2.reset_pins()
    assert bowling_v2.current_pins == 10
    assert bowling_v2.knocked_pins == 0
