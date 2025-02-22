from collections import deque


def bfs(n,k):

    max = 100000

    #시간과 방법의 수를 기록할 배열
    time = [-1] * (max+1)
    ways = [0] * (max+1)

    #수빈이의 시작 위치
    time[n] = 0
    ways[n] = 1

    queue = deque([n])

    while queue:
        x=queue.popleft()

        for nx in [x-1, x+1, 2*x]:
            if 0<= nx <=max:
                #처음 방문하거나 더 적은 시간이 걸리는 경우
                if time[nx] == -1 or time[nx] == time[x]+1:
                    if time[nx] == -1:
                        queue.append(nx)
                    time[nx] = time[x]+1
                    ways[nx]+=ways[x]
    return time[k], ways[k]






n,k = map(int,input().split())
min_time, num_ways = bfs(n, k)

print(min_time)
print(num_ways)
