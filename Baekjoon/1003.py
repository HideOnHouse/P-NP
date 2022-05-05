import sys


def fibonacci(n, table):
    if table[n][0] != -1:
        return table[n]
    else:
        a = fibonacci(n - 1, table)
        b = fibonacci(n - 2, table)
        table[n][0] = a[0] + b[0]
        table[n][1] = a[1] + b[1]
        table[n][2] = a[2] + b[2]
        return table[n]


def main():
    temp = list(map(int, sys.stdin.read().split('\n')[1:-1]))
    for n in temp:
        table = [[-1, -1, -1] for _ in range(max(2, n + 1))]
        table[0] = [0, 1, 0]
        table[1] = [1, 0, 1]
        fibonacci(n, table)
        sys.stdout.write(f"{table[n][1]} {table[n][2]}\n")


if __name__ == '__main__':
    main()
