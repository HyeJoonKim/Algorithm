N = int(input())

if (N==1): print(4)
elif (N==2): print(6)
else:
    arr = [0] * (N+1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3,N+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(2 * (arr[N] + arr[N] + arr[N-1]))
