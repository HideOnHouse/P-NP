import sys


def main():
    C, N, = map(int, sys.stdin.readline().rstrip().split())
    ad = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    table = [float('inf')] * (C + 101)
    table[0] = 0
    for cost, customer, in ad:
        for cur_customer in range(customer, C + 101):
            table[cur_customer] = min(table[cur_customer], table[cur_customer - customer] + cost)
    sys.stdout.write(f"{min(table[C:-1])}\n")


if __name__ == '__main__':
    main()
