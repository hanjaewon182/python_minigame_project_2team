"""숫자 야구 — 담당: 팀원 C

[규칙]
- 컴퓨터가 서로 다른 숫자 3개를 정한다. (예: 3 7 1)
- 플레이어가 3자리를 추측하면 스트라이크(숫자·자리 모두 일치),
  볼(숫자만 일치)을 알려 준다. 최대 9번.

[구현 힌트]
- make_answer() -> str
- judge(answer: str, guess: str) -> tuple[int, int]   # (strike, ball)
"""

import random

GAME_NAME = "숫자 야구"


def make_answer() -> str:
    """서로 다른 숫자 3개로 이루어진 정답을 만든다."""
    numbers = random.sample("0123456789", 3)
    return "".join(numbers)


def judge(answer: str, guess: str) -> tuple[int, int]:
    """정답과 추측을 비교하여 스트라이크와 볼 개수를 반환한다."""
    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    return strike, ball


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    answer = make_answer()

    print(f"\n[{GAME_NAME}]")
    print("서로 다른 숫자 3개를 맞혀 보세요.")
    print("최대 9번까지 시도할 수 있습니다.")

    for attempt in range(1, 10):
        while True:
            guess = input(f"{attempt}/9번째 시도: ")

            if len(guess) != 3 or not guess.isdigit():
                print("3자리 숫자를 입력하세요.")
                continue

            if len(set(guess)) != 3:
                print("서로 다른 숫자 3개를 입력하세요.")
                continue

            break

        strike, ball = judge(answer, guess)

        print(f"{strike} 스트라이크, {ball} 볼")

        if strike == 3:
            print("정답입니다!")
            return

    print(f"게임 종료! 정답은 {answer}였습니다.")
