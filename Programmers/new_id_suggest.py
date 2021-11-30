# 신규 아이디 추천
def solution(new_id):
    answer = []
    # 1
    new_id = new_id.lower()
    # 2, 3
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_' or i == '.':
            if i == '.':
                if len(answer) != 0 and answer[-1] != '.':
                    answer.append(i)
            else:
                answer.append(i)
    # 4
    if len(answer) != 0:
        if answer[0] == '.':
            answer.pop(0)
        if answer[-1] == '.':
            answer.pop(-1)
    # 5
    if len(answer) == 0:
        answer.append('a')
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer.pop(-1)
    # 7
    while len(answer) < 3:
        answer.append(answer[-1])
    return "".join(answer)
