"""틱택토 — 담당: 팀원 E

[규칙]
- 2명이 번갈아 X, O 를 3x3 판에 놓는다.
- 가로·세로·대각선으로 세 칸을 먼저 채우면 승리, 판이 가득 차면 무승부.

[구현 힌트]
- check_winner(board: list[list[str]]) -> str | None   # "X" | "O" | None
- is_full(board: list[list[str]]) -> bool
"""

from utils import ask_int

GAME_NAME = "틱택토"
EMPTY = " "


def new_board() -> list[list[str]]:
    """빈 3x3 판을 만든다."""
    return [[EMPTY] * 3 for _ in range(3)]


def check_winner(board: list[list[str]]) -> str | None:
    """승자가 있으면 "X" 또는 "O", 없으면 None 을 돌려준다."""
    lines = [list(row) for row in board]
    lines += [[board[r][c] for r in range(3)] for c in range(3)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == 3:
            return line[0]
    return None


def is_full(board: list[list[str]]) -> bool:
    """빈 칸이 하나도 없으면 True."""
    return all(cell != EMPTY for row in board for cell in row)


def render(board: list[list[str]]) -> str:
    """판을 문자열로 만든다. 빈 칸에는 칸 번호를 보여준다."""
    rows = []
    for r in range(3):
        cells = []
        for c in range(3):
            cell = board[r][c]
            cells.append(cell if cell != EMPTY else str(r * 3 + c + 1))
        rows.append(" " + " | ".join(cells))
    return "\n---+---+---\n".join(rows)


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    board = new_board()
    player = "X"
    print(f"=== {GAME_NAME} ===")
    while True:
        print(render(board))
        pos = ask_int(f"{player} 차례 - 칸 번호(1~9): ", 1, 9) - 1
        row, col = divmod(pos, 3)
        if board[row][col] != EMPTY:
            print("이미 채워진 칸입니다. 다른 칸을 고르세요.")
            continue
        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print(render(board))
            print(f"{winner} 승리!")
            return
        if is_full(board):
            print(render(board))
            print("무승부!")
            return
        player = "O" if player == "X" else "X"
