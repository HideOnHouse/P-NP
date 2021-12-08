# 지형 이동
import heapq


def solution(land, height):
    visited = [[0] * len(land) for _ in range(len(land))]
    queue = [(0, 0, 0)]
    answer = 0
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        val, x, y = heapq.heappop(queue)
        if visited[x][y]:
            continue

        visited[x][y] = 1
        answer += val

        current_height = land[x][y]

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if max(nx, ny) >= len(land) or min(nx, ny) < 0:
                continue

            next_height = land[nx][ny]
            """
            사다리 없이 방문이 가능한 경우 첫번째 값에 0을 주어서 사다리 없이 방문 가능한 모든 좌표를 방문하고 나면,
            그 다음에 사다리를 설치했을 때 최소의 비용으로 방문 가능한 좌표에 오게 된다.
            """
            require = abs(next_height - current_height)
            if require > height:
                heapq.heappush(queue, (require, nx, ny))
            else:
                heapq.heappush(queue, (0, nx, ny))

    return answer


if __name__ == '__main__':
    print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
