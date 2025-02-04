arr = sorted(int(input()) for _ in range(9))
sum_ = sum(arr)

# 9난장이의 모든 키의 합에서 2명을 뺀 값이 100
for i in range(9):
    for j in range(i+1,9):
        if sum_ - arr[i] - arr[j] == 100:
            for k in range(9):   #2명을 빼고 출력
                if k != i and k != j:
                    print(arr[k])
            exit()