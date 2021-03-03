from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
q = deque()

for i in range(n):
    s = input()
    for j in s:
        graph[i].append(int(j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
number = 0
total = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            cnt = 1
            graph[i][j] = 0
            q.append((i,j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (0<=nx<n and 0<=ny<n) and graph[nx][ny] != 0:
                        q.append((nx,ny))
                        graph[nx][ny] = 0
                        cnt += 1
            number += 1
            total.append(cnt)
print(number)
if number == 0:
    print(0)
else:
    for i in sorted(total):
        print(i)
