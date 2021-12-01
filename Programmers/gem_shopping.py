# 보석 쇼핑
def solution(gems):
    # initial value
    answer = [1, len(gems)]
    n = len(set(gems))
    min_len = answer[1] - answer[0]

    for i in range(len(gems)):
        # shopping
        cart = dict()
        temp = [0, i + 1]
        for j in range(i + 1):
            gem = gems[j]
            if gem in cart:
                cart[gem] += 1
            else:
                cart[gem] = 1

        # reduce length
        if len(cart.keys()) == n:
            print(cart)
            while temp[0] != i:
                gem = gems[temp[0]]
                cart[gem] -= 1
                if cart[gem] != 0:
                    temp[0] += 1
                else:
                    print(cart)
                    break
            current_len = temp[1] - temp[0]
            temp[0] += 1
            if current_len <= min_len:
                if temp[0] < answer[0]:
                    answer = temp
    return answer
