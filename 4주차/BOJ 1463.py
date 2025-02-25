def min_operations(n):
    dp = [0]*(n+1)  # dp[i] : i를 1로 만드는 최소 연산 횟수

    for i in range(2,n+1):
        dp[i] = dp[i-1] +1  # 기본적으로 1을 빼는 경우_ 연산횟수만 1 더해줌

        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)  #1을 뺀 경우와 비교 하여 최소값 갱신

        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1) #1을 뺀 경우 또는 2로 나눈 경우 와 비교 , 3으로 나누어 떨어지면 최소값 갱신

    return dp[n]

n=int(input())
print(min_operations(n))