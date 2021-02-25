# 다 풀어놓고 소수점 3째자리까지 '무조건' 표현하라는 말 지나쳐서 시간 낭비
# 이 기회에 소수점 n째 자리까지 무조건 출력하게 만드는 방법 배움

# 알고리즘은 다른 블로그 참고 + 직접 구현

n = int(input())

dp = [1]*(n+1)

for i in range(1,n+1):
    item = float(input())
    new = dp[i-1]*item
    if new > item:
        dp[i] = new
    else:
        dp[i] = item
        
print('%.3f' %round(max(dp[1:]),3))
