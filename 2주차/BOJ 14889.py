import sys


def calculate_score(team, S):
    """ 주어진 팀의 능력치 합을 계산하는 함수 """
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score


def backtrack(idx, start_team, N, S, min_diff):
    """ 백트래킹을 이용해 팀을 나누고 최솟값을 갱신하는 함수 """
    if len(start_team) == N // 2:
        link_team = [i for i in range(N) if i not in start_team]  #스타트 팀에 속하지 않은 사람들을 모아 링크 팀 만듬

        start_score = calculate_score(start_team, S)
        link_score = calculate_score(link_team, S)

        return min(min_diff, abs(start_score - link_score))

    for i in range(idx, N):
        start_team.append(i)
        min_diff = backtrack(i + 1, start_team, N, S, min_diff)
        start_team.pop()  # 백트래킹

    return min_diff


def solve():
    """ 입력을 받아서 최소 능력치 차이를 계산하는 메인 함수 """
    N = int(input())
    S = [tuple(map(int, input().split())) for _ in range(N)]

    # 최솟값 초기화
    min_diff = float('inf')

    # 백트래킹 시작
    min_diff = backtrack(0, [], N, S, min_diff)

    print(min_diff)

