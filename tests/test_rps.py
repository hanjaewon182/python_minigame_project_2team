"""Tests for the rock-paper-scissors round rules."""

import pytest

from games.rps import decide


@pytest.mark.parametrize(
    "player, computer, expected",
    [
        ("1", "1", "draw"),
        ("2", "2", "draw"),
        ("3", "3", "draw"),
        ("1", "3", "win"),
        ("2", "1", "win"),
        ("3", "2", "win"),
        ("1", "2", "lose"),
        ("2", "3", "lose"),
        ("3", "1", "lose"),
    ],
)
def test_decide(player, computer, expected):
    """Check all nine possible combinations."""
    assert decide(player, computer) == expected


@pytest.mark.parametrize(
    "player, computer",
    [
        ("0", "1"),
        ("1", "4"),
        ("hello", "2"),
        ("3", ""),
    ],
)
def test_invalid_choices(player, computer):
    """Invalid choices should raise a clear error."""
    with pytest.raises(ValueError):
        decide(player, computer)
