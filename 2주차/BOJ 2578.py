
def check_bingo(board):
    count = 0

    # 가로줄 검사
    for row in board:
        if all(x == 0 for x in row):
            count += 1

    # 세로줄 검사
    for col in range(5):
        if all(board[row][col] == 0 for row in range(5)):
            count += 1

    # 대각선 검사
    if all(board[i][i] == 0 for i in range(5)):
        count += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        count += 1

    return count >= 3


def bingo_game(board, calls):
    position = {}
    for i in range(5):
        for j in range(5):
            position[board[i][j]] = (i, j)

    for turn, num in enumerate(calls, 1):
        if num in position:
            x, y = position[num]
            board[x][y] = 0  # 지우기
            if check_bingo(board):
                return turn

    return -1  # 이론상 도달하지 않음


board = [list(map(int, input().split())) for _ in range(5)]
calls = [num for _ in range(5) for num in map(int, input().split())]

print(bingo_game(board, calls))


