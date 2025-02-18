from collections import deque
import sys

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


n,m = map(int,input().split())
graph = {i: [] for i in range(1,n+1)}
visited = {i: False for i in range(1,n+1)}

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#연결 요소 개수 세기
count = 0
for node in range(1, n+1):
    if not visited[node]:  #false면
        bfs(node)
        count+=1    # 새로운 연결 요소 발견

print(count)