# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = [1, 7]
    for i in lottos:
        if i in win_nums:
            answer[1] -= 1
        else:
            if i != 0:
                answer[0] += 1
    answer[0] = min(6, answer[0])
    answer[1] = min(6, answer[1])
    return answer
