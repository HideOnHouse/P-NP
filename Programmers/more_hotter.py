# 더 맵게
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        answer += 1
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        temp = first + (second * 2)
        heapq.heappush(scoville, temp)
    return answer
