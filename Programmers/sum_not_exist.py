# 없는 숫자 더하기
def solution(numbers):
    answer = 45 - sum(set(numbers))
    return answer
