from collections import deque
import sys
input = sys.stdin.readline  # 빠른 입력

# 이동할 네 가지 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(x, y, field, visited, n, m):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 내에 있고, 배추가 있으며, 아직 방문하지 않은 곳
            if 0 <= nx < n and 0 <= ny < m:
                if field[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 입력
t = int(input())

for _ in range(t):
    m,n,k = map(int,input().split())    # 가로, 세로, 배추 개수

    # 배추밭 초기화
    field = [[0]* m for _ in range(n)]
    visited = [[False]* m for _ in range(n)]

    # 배추 위치 입력
    for _ in range(k):
        x,y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0  # 지렁이 수

    # 모든 위치 탐색
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j, field, visited, n, m)
                worm_count += 1

    # 결과 출력
    print(worm_count)
