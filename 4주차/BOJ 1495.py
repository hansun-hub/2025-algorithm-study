import sys
input = sys.stdin.read

# 입력 받기
data = input().split("\n")
N, S, M = map(int, data[0].split())
V = list(map(int, data[1].split()))

# DP 테이블 초기화
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True  # 시작 볼륨 설정

# DP 수행
for i in range(N):  # i번째 곡
    for j in range(M + 1):  # 현재 볼륨 j
        if dp[i][j]:  # 이전 곡에서 j 볼륨이 가능하다면
            if j + V[i] <= M:  # 볼륨 올리기 가능하면
                dp[i + 1][j + V[i]] = True
            if j - V[i] >= 0:  # 볼륨 낮추기 가능하면
                dp[i + 1][j - V[i]] = True

# 마지막 곡에서 가능한 최대 볼륨 찾기
answer = -1
for j in range(M, -1, -1):  # 큰 값부터 탐색
    if dp[N][j]:
        answer = j
        break

print(answer)
