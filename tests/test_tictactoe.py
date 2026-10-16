from games.tictactoe import check_winner, is_full, new_board


def test_row_win():
    board = [["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
    assert check_winner(board) == "X"


def test_column_win():
    board = [["O", "X", " "], ["O", "X", " "], ["O", " ", "X"]]
    assert check_winner(board) == "O"


def test_diagonal_win():
    board = [["X", "O", " "], ["O", "X", " "], [" ", " ", "X"]]
    assert check_winner(board) == "X"


def test_no_winner():
    assert check_winner(new_board()) is None


def test_is_full():
    board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    assert is_full(board)
    assert check_winner(board) is None


def test_is_not_full():
    assert not is_full(new_board())
