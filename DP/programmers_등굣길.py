def solution(m, n, puddles):
    arr = [[0 for _ in range(m)] for _ in range(n) ]
    if puddles:
        for puddle in puddles:
            arr[puddle[1]-1][puddle[0]-1] = -1
            
    for i in range(m):
        if arr[0][i] == -1:
            break
        arr[0][i] = 1
        
    for i in range(n):
        if arr[i][0] == -1:
            break
        arr[i][0] = 1
        
        
    for y in range(1,n):
        for x in range(1,m):
            if arr[y][x] == -1:
                continue
                
            if arr[y-1][x] == -1 and arr[y][x-1] == -1:
                arr[y][x] = 0                
            elif arr[y-1][x] == -1:
                arr[y][x] = arr[y][x-1]
            elif arr[y][x-1] == -1:
                arr[y][x] = arr[y-1][x]            
            else:
                arr[y][x] = arr[y-1][x] + arr[y][x-1]
    
    return arr[n-1][m-1] % 1000000007
