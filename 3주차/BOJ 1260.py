from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for neighbor in sorted(graph[v]):  # 작은 번호부터 방문
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def bfs(graph, v):
    queue = deque([v])
    visited = {node: False for node in graph}
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in sorted(graph[node]):  # 작은 번호부터 방문
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


# 입력 받기
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = {i: False for i in range(1, n + 1)}
dfs(graph, v, visited)
print()
bfs(graph, v)
