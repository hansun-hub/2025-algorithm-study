import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    grid[x][y] = 0  # 방문 처리
    count = 1  # 현재 집 포함

    # 상하좌우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                count += 1

    return count


N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]

complexes = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            complexes.append(bfs(i, j))

complexes.sort()

print(len(complexes))
for size in complexes:
    print(size)