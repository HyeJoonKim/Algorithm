N = int(input())

cnt = 0

while (N >= 3):
    if (N % 5 == 0):
        cnt = cnt + (N // 5)
        N = 0
        break
    else:
        cnt += 1
        N = N - 3
       
if (N==0):
    print(cnt)
else:
    print(-1)
