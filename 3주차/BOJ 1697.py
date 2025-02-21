from collections import deque


def bfs(n, k):
    if n == k:
        return 0

    max_pos = 100000
    visited = [-1] * (max_pos + 1)
    queue = deque([n])
    visited[n] = 0

    while queue:
        x = queue.popleft()
        for next_pos in (x - 1, x + 1, 2 * x):
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[x] + 1
                if next_pos == k:
                    return visited[next_pos]
                queue.append(next_pos)

    return -1


# 입력 받기
n, k = map(int, input().split())
print(bfs(n, k))
