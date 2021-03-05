import heapq
def solution(operations):
    max_h = []  # 최댓값 삭제
    min_h = [] # 최솟값 삭제
    cnt = 0
    
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(max_h,-int(op[2:]))  # heapq는 오름차순이므로 음수를 삽입
            heapq.heappush(min_h,int(op[2:]))
            cnt += 1
            
        else:
            if cnt > 0:   
                if op == 'D 1':
                    heapq.heappop(max_h)
                    cnt -= 1
                elif op == 'D -1':
                    heapq.heappop(min_h)
                    cnt -= 1
                    
    if cnt == 0:
        return [0,0]
    
    result1 = set(min_h)
    result2 = set()
    for i in max_h:
        result2.add(-i)
    result = result1 & result2
    return [max(result),min(result)]
