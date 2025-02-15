from itertools import permutations

# 수식 계산 함수
def calculate(numbers, operators):
    result = numbers[0]
    index = 1
    for operator in operators:
        if operator == '+':
            result += numbers[index]
        elif operator == '-':
            result -= numbers[index]
        elif operator == '*':
            result *= numbers[index]
        elif operator == '/':
            # 나눗셈은 정수 나눗셈, C++14의 음수 나눗셈 규칙 적용
            if result < 0:
                result = -(-result // numbers[index])
            else:
                result //= numbers[index]
        index += 1
    return result

# 입력 받기
N = int(input())  # 수의 개수
numbers = list(map(int, input().split()))  # 수열 A1, A2, ..., AN
add, sub, mul, div = map(int, input().split())  # 연산자 개수

# 연산자 리스트 만들기
operators = ['+'] * add + ['-'] * sub + ['*'] * mul + ['/'] * div

# 연산자의 모든 순열을 생성
perm_operators = set(permutations(operators))

# 최댓값과 최솟값 계산
max_result = -float('inf')
min_result = float('inf')

for perm in perm_operators:
    result = calculate(numbers, perm)
    max_result = max(max_result, result)
    min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)
