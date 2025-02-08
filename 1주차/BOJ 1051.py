def find_largest_square(n,m,grid):
    max_size = 1    #최소 정사각형 크기는 1

    for i in range(n):
        for j in range(m):
            #격자 밖으로 나가지 않게
            for k in range(min(n-i,m-j)):
                if grid[i][j] == grid[i][j+k] == grid[i+k][j] == grid[i+k][j+k]:
                    max_size=max(max_size, (k+1) ** 2) #정사각형 크기 구하기
    return max_size

# 입력처리
n,m = map(int,input().split())
grid = [input().strip() for _ in range(n)]


#결과 출력
print(find_largest_square(n,m,grid))