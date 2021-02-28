# while (s < e) 는 시간 초과 뜸
# DP로 해결

import sys
input = sys.stdin.readline  # 이렇게 해야 시간초과 안뜸

n = int(input())
arr = list(map(int, input().split()))
dp = [[0]* n for _ in range(n)]

for i in range(n):    # 1 자리수
    dp[i][i] = 1
    
for i in range(1,n):    # 2 자리수
    if arr[i] == arr[i-1]:
        dp[i][i-1] = 1
        dp[i-1][i] = 1
        
for i in range(2,n):    # 3 이상
    for j in range(n-i):
        if  arr[j] == arr[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1
            
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
