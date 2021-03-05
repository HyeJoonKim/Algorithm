import heapq
def solution(scoville, K):
    h = []
    for i in scoville:
        heapq.heappush(h,i)
    
    cnt = 0
    while h:
        first = heapq.heappop(h)
        if first >= K:
            return cnt
        if len(h) >= 1:
            second = heapq.heappop(h)
            new = first + (second * 2)
            heapq.heappush(h,new)
            cnt += 1
        
    return -1
