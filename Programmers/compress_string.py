# 문자열 압축
def solution(s):
    answer = []
    for n in range(1, len(s) + 1):
        temp = 0
        count = 0
        head = s[:n]
        for idx in range(0, len(s), n):
            sliced = s[idx:idx + n]
            if sliced == head:
                count += 1
            else:
                if count != 1:
                    temp += len(str(count)) + n
                else:
                    temp += n
                head = sliced
                count = 1
        if count != 1:
            temp += len(str(count)) + len(head)
        else:
            temp += len(head)
        answer.append(temp)
    return min(answer)
