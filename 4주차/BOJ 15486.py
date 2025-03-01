n=int(input())
schdule = [tuple(map(int,input().split())) for _ in range(n)]

dp = [0] * (n+1)

#뒤에서 거꾸로 확인
for day in range(n-1,-1,-1):
    time, pay = schdule[day]
    end_day = day + time

    if end_day <= n:    #상담을 할 수 있는 경우
        dp[day] = max(pay+dp[end_day], dp[day+1])
    else:               #상담을 할 수 없는 경우
        dp[day] = dp[day+1]


#최대 이익 출력
print(dp[0])
