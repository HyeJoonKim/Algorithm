T = int(input())

arr = [0] * T 
for i in range(T):    #횟수 입력 받은 후 list 형태로 n,m 저장
    arr[i] = list(map(int, input().split()))
    
m = max(map(max,arr))    # 입력받은 수 중에서 가장 큰 수 m 얻음
f = [1] * (m+1)           # 큰 수 길이의 배열 생성 (0! = 1 이므로 1로 초기화)
total = 1
for j in range(1,m+1):    # m 까지 팩토리얼 구해서 배열로 저장 (DP)
    total *= j
    f[j] = total
    
for k in range(T):        # m길이의 팩토리얼 배열에서 조합 식에 필요한 원소 가져다 사용
    n,m = arr[k]
    result = f[m] // (f[m-n] * f[n])
    print(result)
