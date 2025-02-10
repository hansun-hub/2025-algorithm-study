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