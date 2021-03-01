# 다리 위에 있는 트럭을 관리할 q를 만드는 것이 핵심
# 시간 경과를 어떻게 표현해야하는지 어려웠는데,
# 0을 q에 push하고 pop 하는 것이 매우 중요했다
# sum(q)는 시간초과가 나서 변수에 계속 더하고 빼야함

from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    q = deque([0 for _ in range(bridge_length)])    # 이렇게 선언 가능
    total_weight = 0
    
    while True:
        
        if not q and not truck_weights:
            break
        
        total_weight -= q.popleft() # 일단 빼고 시작
        
        if truck_weights:
            if total_weight + truck_weights[0] > weight:
                q.append(0)
            else:
                new = truck_weights.pop(0)
                q.append(new)
                total_weight += new
        
        cnt += 1
        
    return cnt
