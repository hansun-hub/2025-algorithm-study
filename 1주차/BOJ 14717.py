from itertools import combinations


def get_rank(card1, card2):
    if card1 == card2:
        return (2, card1)  # 땡 족보 (우선순위 2, 카드 값)
    else:
        return (1, (card1 + card2) % 10)  # 끗 족보 (우선순위 1, 합의 일의 자리)


def calculate_win_probability(A, B):
    all_cards = [i for i in range(1, 11) for _ in range(2)]  # 1~10이 각각 2장씩 존재
    all_cards.remove(A)
    all_cards.remove(B)

    total_cases = 0
    win_cases = 0

    for opp1, opp2 in combinations(all_cards, 2):
        total_cases += 1
        my_rank = get_rank(A, B)
        opp_rank = get_rank(opp1, opp2)

        if my_rank > opp_rank:
            win_cases += 1

    win_probability = win_cases / total_cases
    print(f"{win_probability:.3f}")


# 입력 받기
A, B = map(int, input().split())
calculate_win_probability(A, B)


