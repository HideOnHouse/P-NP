# 단어 퍼즐
def solution(strs, t):
    strs = set(strs)
    table = [float('inf')] * (len(t) + 1)
    table[0] = 0
    for idx in range(1, len(t) + 1):
        for n in range(1, 6):
            s = t[idx - n: idx]
            if s in strs:
                table[idx] = min(table[idx], table[idx - n] + 1)

    answer = table[-1]
    if answer == float('inf'):
        answer = -1
    return answer
