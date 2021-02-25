H, Y = map(int,input().split())

dp = [0]*(Y+1)
dp[0] = H

for i in range(1,Y+1):
    maxn = 0
    rate = 0
    if i-1 >= 0:
        maxn = max(maxn,dp[i-1]*1.05)
    if i-3 >= 0:
        maxn = max(maxn,dp[i-3]*1.2)
    if i-5 >= 0:
        maxn = max(maxn,dp[i-5]*1.35)
    dp[i] = int(maxn)
    
print(dp[Y])   
