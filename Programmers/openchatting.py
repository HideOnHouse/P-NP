# 오픈채팅방
def solution(record):
    uid2nick = dict()
    answer = []
    for log in record:
        temp = log.split(" ")
        if len(temp) == 2:
            command, uid = temp
            answer.append([command, uid])
        else:
            command, uid, nick = temp
            uid2nick[uid] = nick
            if command == 'Enter':
                answer.append([command, uid])
    for i in range(len(answer)):
        nickname = uid2nick[answer[i][1]]
        if answer[i][0] == 'Enter':
            answer[i] = f"{nickname}님이 들어왔습니다."
        else:
            answer[i] = f"{nickname}님이 나갔습니다."
    return answer
