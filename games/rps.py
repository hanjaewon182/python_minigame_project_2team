"""Rock-paper-scissors: first to two wins against the computer."""

import random

GAME_NAME = "가위바위보"
CHOICES = {"1": "Scissors", "2": "Rock", "3": "Paper"}


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

    print("\n[Rock-Paper-Scissors] First to 2 wins!")
    print("Draws do not count. Enter q to return to the menu.")

    while player_score < 2 and computer_score < 2:
        player = input("\n1: Scissors / 2: Rock / 3: Paper / q: Quit > ").strip()

        if player.lower() == "q":
            print("Returning to the menu.")
            return

        if player not in CHOICES:
            print("Invalid input! Please enter 1, 2, 3, or q.")
            continue

        computer = random.choice(list(CHOICES))

        print(f"You: {CHOICES[player]} / Computer: {CHOICES[computer]}")

        result = decide(player, computer)

        if result == "win":
            player_score += 1
            print("You won this round!")
        elif result == "lose":
            computer_score += 1
            print("You lost this round!")
        else:
            print("Draw! Play again.")

        print(f"Score: You {player_score} - Computer {computer_score}")

    if player_score == 2:
        print("\nYou won the match!")
    else:
        print("\nComputer won the match!")
