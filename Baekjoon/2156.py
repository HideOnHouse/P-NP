# 포도주 시식
import sys


def main():
    temp = list(map(int, sys.stdin.read().split('\n')[:-1]))
    wines = [0]
    for i in range(temp[0]):
        wines.append(temp[i + 1])
    if len(wines) == 1:
        print(wines[0])
    elif len(wines) == 2:
        print(wines[0] + wines[1])
    else:
        table = [0] * (len(temp))
        table[1] = wines[1]
        table[2] = wines[1] + wines[2]
        for i in range(3, len(temp)):
            table[i] = max([
                table[i - 1],
                wines[i] + table[i - 2],
                wines[i] + wines[i - 1] + table[i - 3],
            ])
        print(table[temp[0]])


if __name__ == '__main__':
    main()
