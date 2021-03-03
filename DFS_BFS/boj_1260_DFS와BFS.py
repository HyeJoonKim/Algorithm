from collections import deque

def dfs(graph,start,arr):
    arr[start] = 1
    print(start,end=' ')
    for j in graph[start]:        
        if arr[j] == 0:
            dfs(graph, j ,arr) 
       
    
def bfs(graph,start,arr):
    q = deque([start])
    arr[start] = 1
    while q:
        item = q.popleft()
        print(item, end=' ')
        for i in graph[item]:
            if arr[i] == 0:
                q.append(i)
                arr[i] = 1
        
    
n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,n+1):
    g[i] = sorted(g[i])
    
visited = [0] * (n+1)
dfs(g,v,visited)
print()
visited = [0] * (n+1)
bfs(g,v,visited)
