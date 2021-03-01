import math
from collections import deque
def solution(progresses, speeds):
    
    time = deque()
    for p,s in zip(progresses, speeds):
        time.append(math.ceil((100-p)/s))
    
    result = []
    while time:
        cnt = 1     # pop 하면 무조건 1개부터
        now = time.popleft()
        while time and (now >= time[0]) :   # 순서 바뀌면 에러;;
            time.popleft()
            cnt += 1
        result.append(cnt)
    return result
