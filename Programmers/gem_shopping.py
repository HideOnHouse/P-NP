# 보석 쇼핑
def solution(gems):
    answer = [0, len(gems)]
    n = len(set(gems))
    cart = dict()
    min_len = len(gems)
    temp = [0, 0]
    while temp[1] < len(gems):
        # shopping
        gem = gems[temp[1]]
        if gem in cart:
            cart[gem] += 1
        else:
            cart[gem] = 1
        temp[1] += 1

        # meet condition
        if len(cart.keys()) == n:
            # reduce length
            while temp[0] < temp[1]:
                gem = gems[temp[0]]
                if cart[gem] == 1:
                    break
                else:
                    cart[gem] -= 1
                temp[0] += 1
            # compare with answer
            cur_len = temp[1] - temp[0]
            if cur_len < min_len:
                answer = temp[::]  # deep copy makes me to solve this problem for 2 hours
                min_len = cur_len
    return answer
