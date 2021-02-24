# pypy3 로 돌려야 시간초과 X
# python3 는 시간초과 발생 (0.5s)

n=int(input())
dp=[0,1]

for j in range(2,n+1):
    minn=50000
    k=1
    while ((k*k) <= j):
        minn = min(dp[j-k*k],minn)
        k += 1
    dp.append(minn+1)    
print(dp[n])
