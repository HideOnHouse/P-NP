# 바이러스


def main():
    n = int(input())
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    distances = dict()
    for _ in range(int(input())):
        i, j = map(int, input().split(' '))
        adj_matrix[i - 1][j - 1] = 1
        adj_matrix[j - 1][i - 1] = 1
    distances[0] = adj_matrix
    for k in range(1, n + 1):
        distances[k] = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                distances[k][i][j] = min(distances[k - 1][i][j],
                                         distances[k - 1][i][k - 1] + distances[k - 1][k - 1][j])

    print(len(distances[n][0]) - distances[n][0].count(float('inf')) - 1)


if __name__ == '__main__':
    main()
