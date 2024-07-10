import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        n3 = n1 + n2 * 2
        heapq.heappush(scoville, n3)
        cnt += 1
    return cnt