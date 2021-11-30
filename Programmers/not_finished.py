# 완주하지 못한 선수
def solution(participant, completion):
    count = dict()
    for i in completion:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in participant:
        if i in count:
            count[i] -= 1
            if count[i] == -1:
                return i
        else:
            return i
