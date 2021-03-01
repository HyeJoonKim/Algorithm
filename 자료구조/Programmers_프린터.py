from collections import deque
def solution(p, l):
    
    q = deque()
    cnt = 0
    
    for index, element in enumerate(p):
        q.append((element,index))
    
    while q:
        item, idx = q.popleft()
        maxx = max(p)
        if item == maxx:        # 여기서 가장 오래 고민
            p.pop(p.index(maxx))
            cnt += 1
            if idx == l:
                return cnt
        else:
            q.append((item,idx))
