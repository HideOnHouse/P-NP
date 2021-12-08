def solution(gems):
    answer = [0, len(gems) - 1]
    n = len(set(gems))
    temp = [0, 0]
    cart = dict()
    # shopping
    while temp[1] < len(gems):
        gem = gems[temp[1]]
        if gem in cart:
            cart[gem] += 1
        else:
            cart[gem] = 1
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
            if (temp[1] - temp[0]) < (answer[1] - answer[0]):
                answer = temp[::]
        temp[1] += 1
    answer[0] += 1
    answer[1] += 1
    return answer
