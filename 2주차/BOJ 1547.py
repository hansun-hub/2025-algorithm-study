# 내 코드
cup= [0]*3
cup[0]=1

def bounce(x,y):
    temp=cup[x-1]
    cup[x - 1] = cup[y-1]
    cup[y-1] = temp

m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    bounce(x,y)
index = [i for i,v in enumerate(cup) if v==1]
print(int(*index)+1)

#############################################
#개선된 코드
M = int(input())
# 컵의 초기 위치 설정 (1번 컵에 공이 있음)
cups = [1, 2, 3]

for _ in range(M):
    X, Y = map(int, input().split())
    # 인덱스를 맞추기 위해 -1을 해줌
    idx_X, idx_Y = cups.index(X), cups.index(Y)
    cups[idx_X], cups[idx_Y] = cups[idx_Y], cups[idx_X]

# 공이 있는 컵 찾기 (초기 위치는 1번 컵)
print(cups.index(1) + 1)