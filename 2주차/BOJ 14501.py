def max_profit(N, schedule):
    dp = [0] * (N + 2)  # N+1까지 필요하므로 N+2 크기 할당

    # 뒤에서부터 dp 갱신
    for day in range(N, 0, -1):
        time, pay = schedule[day - 1]  # 상담 기간, 이익
        next_day = day + time  # 상담이 끝나는 날

        if next_day <= N + 1:  # 상담 가능
            dp[day] = max(dp[day + 1], pay + dp[next_day])
        else:  # 상담 불가능
            dp[day] = dp[day + 1]

    return dp[1]  # 1일부터 시작할 때 최대 이익 반환

# 입력 처리
N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
print(max_profit(N, schedule))









