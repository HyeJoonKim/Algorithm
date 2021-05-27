import heapq

def solution(a):
    min_q = []
    max_q = []

    for element in a:
        heapq.heappush(min_q,element)
        heapq.heappush(max_q,-element)

    result = 0
    cnt = 0
    if len(a) % 2 == 0:
        while cnt <= len(a):
            if cnt % 2 == 0:
                result -= heapq.heappop(min_q)
                cnt += 1
            else:
                result -= heapq.heappop(max_q)
                cnt += 1
                       
    else:
        while cnt <= len(a):
            if cnt % 2 != 0:
                result -= heapq.heappop(min_q)
                cnt += 1
            else:
                result -= heapq.heappop(max_q)
                cnt += 1

    return result
        
    
        
