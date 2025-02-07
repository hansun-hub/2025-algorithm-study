def count_repaints(board, start_row, start_col, first_color):
    repaint_count = 0
    for i in range(8):
        for j in range(8):
            expected_color = first_color if (i+j) % 2 == 0 else ('B' if first_color == 'W' else 'W')
            if board[start_row+i][start_col + j] != expected_color:
                repaint_count +=1
    return repaint_count

def min_repaints_to_chessboard(board, n, m):
    min_repaint = float('inf')
    for i in range(n-7):
        for j in range(m-7):
            repaints_white_start = count_repaints(board, i, j, 'W')
            repaints_black_start = count_repaints(board,i,j,'B')
            min_repaint = min(min_repaint, repaints_white_start, repaints_black_start)
    return min_repaint


# 입력 받기
n, m = map(int,input().split())
board = [input().strip() for _ in range(n)]

#결과출력
print(min_repaints_to_chessboard(board,n,m))


