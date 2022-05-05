def solution(n, stations, w):
    """

    :param n: 도시 길이
    :param stations: 기지국 상태 저장 배열
    :param w: 기지국의 범위
    :return:
    """
    answer = 0
    idx = 0  # station index
    i = 1  # current idx
    while i <= n:
        # 기지국 범위에 있으면
        if idx < len(stations) and stations[idx] - w <= i <= stations[idx] + w:
            i = stations[idx] + w + 1
            idx += 1
        else:
            # 기지국 설치하고 넘어감
            i += 2 * w + 1
            answer += 1
    return answer
