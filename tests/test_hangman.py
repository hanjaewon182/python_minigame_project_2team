"""행맨 순수 함수 테스트 — 담당: 2026100529 홍성민  (저장 위치: tests/test_hangman.py)"""

from games import hangman


def test_mask_word_none_guessed():
    assert hangman.mask_word("apple", set()) == "_ _ _ _ _"


def test_mask_word_partial():
    assert hangman.mask_word("apple", {"a", "p"}) == "a p p _ _"


def test_mask_word_all():
    assert hangman.mask_word("apple", set("apple")) == "a p p l e"


def test_is_solved_true():
    assert hangman.is_solved("apple", set("aple")) is True


def test_is_solved_false():
    assert hangman.is_solved("apple", {"a", "p"}) is False


def test_count_wrong():
    assert hangman.count_wrong("apple", {"a", "z", "x"}) == 2
    assert hangman.count_wrong("apple", set()) == 0


def test_pick_word_from_list():
    assert hangman.pick_word(["only"]) == "only"
    assert hangman.pick_word() in hangman.WORDS


def test_validate_guess_ok_and_case_insensitive():
    assert hangman.validate_guess(" A ", set()) == ("a", "")


def test_validate_guess_invalid_inputs():
    for raw in ["", "ab", "1", "가", "!"]:
        letter, message = hangman.validate_guess(raw, set())
        assert letter is None
        assert message


def test_validate_guess_duplicate():
    letter, message = hangman.validate_guess("a", {"a"})
    assert letter is None
    assert "이미" in message


def test_play_win(monkeypatch, capsys):
    monkeypatch.setattr(hangman, "pick_word", lambda *a: "ab")
    inputs = iter(["a", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    hangman.play()
    assert "정답" in capsys.readouterr().out


def test_play_lose_with_bad_inputs(monkeypatch, capsys):
    monkeypatch.setattr(hangman, "pick_word", lambda *a: "ab")
    inputs = iter(["", "1", "xx", "c", "c", "d", "e", "f", "g", "h"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    hangman.play()
    assert "실패" in capsys.readouterr().out
