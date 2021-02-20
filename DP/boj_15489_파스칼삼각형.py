R, C, W = map(int, input().split())

triArr = [[1] for _ in range(R+W)]      # 2차원 배열 생성
triArr[2].append(1)     # 삼각형의 양 끝은 1

# 삼각형 생성
for i in range(3,R+W):
    for j in range(i-2):
        sum = triArr[i-1][j] + triArr[i-1][j+1]
        triArr[i].append(sum)
    triArr[i].append(1)     # 삼각형의 양 끝은 1

result = 0
for i in range(R,R+W):      # 한 줄씩 내려갈때마다 더하는 개수가 1씩 증가해야함
    for j in range(i-R+1):
        result += triArr[i][C-1+j]
        
print(result)
