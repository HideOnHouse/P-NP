import sys
from math import comb


def main():
    temp = sys.stdin.read().split('\n')[1:-1]
    for i in temp:
        n, r = map(int, i.split(' '))
        sys.stdout.write(f"{comb(r, n)}\n")


if __name__ == '__main__':
    main()
