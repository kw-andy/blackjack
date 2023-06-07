import pytest

from blackjack.common import card_score


@pytest.mark.parametrize("cards, score", [("KK", 20), ("JKQ", 0), ("AK", 21), ("AA", 12)])
def test_simple_case_1(cards, score):
    assert card_score(cards) == score

def test_number_of_cards1():
    with pytest.raises(ValueError):
        card_score("")

def test_number_of_cards2():
    with pytest.raises(ValueError):
        card_score(2)