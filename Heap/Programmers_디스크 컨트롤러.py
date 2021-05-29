import heapq
def solution(jobs):
    jobs.sort()
    time = 0
    now = 0
    n = len(jobs)
    while jobs:
        h = []
        for i in range(len(jobs)):
            if jobs[i][0] > now:
                break
            heapq.heappush(h,(jobs[i][1], jobs[i][0], i))
            
        if not h:
            now += 1
            continue
            
        time += now-h[0][1]+h[0][0]
        now += h[0][0]
        jobs.pop(h[0][2])
    return time//n
