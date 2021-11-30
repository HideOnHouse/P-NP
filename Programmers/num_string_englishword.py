# 숫자 문자열과 영단어
def solution(s: str):
    for idx, i in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        s = s.replace(i, str(idx))
    return int(s)
