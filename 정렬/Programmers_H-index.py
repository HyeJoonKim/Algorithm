def solution(citations):
    citations.sort()
        
    if  citations[-1] == 0:
        return 0
    if citations[-1] == 1:
        return 1
    if len(citations) == 1:
        return 0
    
    maxx = -1
    for i in range(citations[-1]+1):
        cnt = 0
        for c in citations:
            if i <= c:
                cnt += 1
        if i <= cnt:
            maxx = max(maxx, i)
    return maxx
