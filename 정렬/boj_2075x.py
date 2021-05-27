import heapq    # 메모리 제한 있었다
 
N = int(input())
h = []

for i in range(N):
    arr = list(map(int, input().split()))
    
    if not h:
        for i in arr:
            heapq.heappush(h, i)
    else:
        for i in arr:
            if h[0] < i:
                heapq.heappop(h)
                heapq.heappush(h,i)

print(h[0])
