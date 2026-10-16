"""Rock-paper-scissors: first to two wins against the computer."""

import random

GAME_NAME = "가위바위보"
CHOICES = {"1": "가위", "2": "바위", "3": "보"}


def decide(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'draw' for one round."""
    if player not in CHOICES or computer not in CHOICES:
        raise ValueError("Choices must be '1', '2', or '3'.")

    if player == computer:
        return "draw"

    # Scissors beat paper, rock beats scissors, paper beats rock.
    winning_pairs = {("1", "3"), ("2", "1"), ("3", "2")}

    if (player, computer) in winning_pairs:
        return "win"

    return "lose"


def play() -> None:
    """Play until either side wins twice, then return to the menu."""
    player_score = 0
    computer_score = 0

    print(f"\n[{GAME_NAME}] 먼저 2승을 하면 승리합니다!")
    print("무승부는 점수에 포함되지 않습니다. q를 입력하면 메뉴로 돌아갑니다.")

    while player_score < 2 and computer_score < 2:
        player = input("\n1: 가위 / 2: 바위 / 3: 보 / q: 종료 > ").strip()

        if player.lower() == "q":
            print("메인 메뉴로 돌아갑니다.")
            return

        if player not in CHOICES:
            print("잘못된 입력입니다! 1, 2, 3 또는 q를 입력하세요.")
            continue

        computer = random.choice(list(CHOICES))

        print(f"나: {CHOICES[player]} / 컴퓨터: {CHOICES[computer]}")

        result = decide(player, computer)

        if result == "win":
            player_score += 1
            print("이번 판에서 이겼습니다!")
        elif result == "lose":
            computer_score += 1
            print("이번 판에서 졌습니다!")
        else:
            print("무승부입니다! 다시 진행합니다.")

        print(f"점수: 나 {player_score} - 컴퓨터 {computer_score}")

    if player_score == 2:
        print("\n최종 승리했습니다!")
    else:
        print("\n컴퓨터가 최종 승리했습니다!")
