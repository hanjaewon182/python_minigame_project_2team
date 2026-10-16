"""행맨 — 담당: 2026100529 홍성민

[규칙]
- 단어 목록에서 무작위로 하나를 고른다.
- 플레이어는 한 글자씩 추측하고, 틀리면 기회가 하나 줄어든다. (기회 6번)
- 맞힌 글자만 보여 준다.  예) a _ p l _

[구현 힌트] 테스트하기 쉽도록 순수 함수로 나눠 보세요.
- mask_word(word: str, guessed: set[str]) -> str
- is_solved(word: str, guessed: set[str]) -> bool
"""

import random

GAME_NAME = "행맨"

MAX_WRONG = 6
WORDS = [
    "apple",
    "banana",
    "python",
    "github",
    "branch",
    "commit",
    "merge",
    "review",
    "keyboard",
    "program",
    "computer",
    "variable",
    "function",
    "terminal",
    "algorithm",
]

# 틀린 횟수(0~6)별 그림
STAGES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def mask_word(word: str, guessed: set[str]) -> str:
    """맞힌 글자만 보여 주고 나머지는 _ 로 가린다. 예) 'apple' -> 'a _ _ _ _'"""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 글자를 맞혔는지 여부."""
    return all(ch in guessed for ch in word)


def count_wrong(word: str, guessed: set[str]) -> int:
    """지금까지 틀린 글자 수."""
    return sum(1 for g in guessed if g not in word)


def pick_word(words: list[str] = WORDS) -> str:
    """단어 목록에서 무작위로 하나를 고른다."""
    return random.choice(words)


def validate_guess(raw: str, guessed: set[str]) -> tuple[str | None, str]:
    """입력을 검사한다. (정규화된 글자 또는 None, 안내 메시지)를 돌려준다."""
    text = raw.strip().lower()
    if len(text) != 1:
        return None, "한 글자만 입력하세요."
    if not ("a" <= text <= "z"):
        return None, "영문 알파벳만 입력할 수 있습니다."
    if text in guessed:
        return None, "이미 추측한 글자입니다."
    return text, ""


def _show_status(word: str, guessed: set[str]) -> None:
    wrong = count_wrong(word, guessed)
    wrong_letters = sorted(g for g in guessed if g not in word)
    print()
    print(STAGES[min(wrong, len(STAGES) - 1)])
    print(f"단어: {mask_word(word, guessed)}")
    print(f"틀린 글자: {' '.join(wrong_letters) if wrong_letters else '-'}")
    print(f"남은 기회: {MAX_WRONG - wrong}")


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    word = pick_word()
    guessed: set[str] = set()
    print(f"\n[{GAME_NAME}] 단어를 맞혀 보세요! (기회 {MAX_WRONG}번)")

    while True:
        _show_status(word, guessed)
        if is_solved(word, guessed):
            print(f"\n🎉 정답입니다! 단어는 '{word}' 였습니다.")
            return
        if count_wrong(word, guessed) >= MAX_WRONG:
            print(f"\n💀 실패했습니다. 정답은 '{word}' 였습니다.")
            return

        try:
            raw = input("글자를 입력하세요: ")
        except (EOFError, KeyboardInterrupt):
            print("\n입력이 종료되어 게임을 마칩니다.")
            return

        letter, message = validate_guess(raw, guessed)
        if letter is None:
            print(message)
            continue

        guessed.add(letter)
        if letter in word:
            print(f"'{letter}' 맞았습니다!")
        else:
            print(f"'{letter}' 는 없습니다.")


if __name__ == "__main__":
    play()
