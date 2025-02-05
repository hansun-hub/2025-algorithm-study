tri = [i*(i+1)//2 for i in range(1,46)]
arr=[0]*1001

for i in tri:
    for j in tri:
        for k in tri:
            num=i+j+k
            if num <= 1000:
                arr[num]=1

n=int(input())
for _ in range(n):
    print(arr[int(input())])