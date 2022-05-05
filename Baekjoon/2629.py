import sys


def main():
    num_weight = int(sys.stdin.readline().rstrip())
    weights = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    num_marble = int(sys.stdin.readline().rstrip())
    marbles = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    """
    1106번 advertise 랑 비슷한 weights marbles
    """
    dp = [0] * 40001
    dp[weights[0]] = 1
    for i in range(1, len(weights)):
        temp = [weights[i]]
        for j in range(1, len(dp)):
            if dp[j] != 0:
                idx = abs(j - weights[i])
                if idx < 40001:
                    temp.append(idx)
                idx = abs(j + weights[i])
                if idx < 40001:
                    temp.append(idx)
        for j in temp:
            dp[j] = 1
    for i in marbles:
        if dp[i]:
            sys.stdout.write("Y ")
        else:
            sys.stdout.write("N ")
    print()


if __name__ == '__main__':
    main()
