from games.baseball import make_answer, judge


def test_make_answer():
    answer = make_answer()

    assert len(answer) == 3
    assert answer.isdigit()
    assert len(set(answer)) == 3


def test_three_strikes():
    assert judge("371", "371") == (3, 0)


def test_one_strike_two_balls():
    assert judge("371", "317") == (1, 2)


def test_two_balls():
    assert judge("371", "123") == (0, 2)


def test_no_match():
    assert judge("371", "456") == (0, 0)
