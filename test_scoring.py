"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating
from scoring_helpers import apply_streak_bonus


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


def test_session_rating_boundary_70_is_ok():
    assert session_rating(70) == "OK"


def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"


def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"


def test_session_rating_negative_score_is_skip():
    assert session_rating(-122) == "Skip"


def test_session_rating_float_score():
    assert session_rating(91.5) == "Great"


def test_session_rating_string_score():
    assert session_rating('a') == "Skip"


def test_session_rating_boolean_score():
    assert session_rating(True) == "Skip"


def test_apply_streak_bonus_normal():
    assert apply_streak_bonus(50, 3) == 56


def test_apply_streak_bonus_cap_at_100():
    assert apply_streak_bonus(95, 5) == 100


def test_apply_streak_bonus_zero_streak():
    assert apply_streak_bonus(50, 0) == 50
