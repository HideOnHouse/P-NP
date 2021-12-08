# 1로 만들기


def main():
    x = int(input())
    table = [-1] * max(x + 1, 4)
    table[1], table[2], table[3] = 0, 1, 1
    for i in range(4, x + 1):
        temp = 1000000
        """
        if x < 3 --> x = 1
        else x + 1 = min(x // 3, x // 2, x - 1)
        """
        if i % 3 == 0:
            temp = min(table[i // 3], temp)
        if i % 2 == 0:
            temp = min(table[i // 2], temp)
        temp = min(table[i - 1], temp)
        table[i] = temp + 1
    answer = table[x]
    print(answer)


if __name__ == '__main__':
    main()
