def solution(N, number):
    arr = [set([int(str(N)*(i+1))]) for i in range(8)]
    
    if number == N:
        return 1
    
    for i in range(1,8):
        for j in range(i):
            for e1 in arr[j]:
                for e2 in arr[i-j-1]:
                    arr[i].add(e1+e2)
                    arr[i].add(e1-e2)
                    arr[i].add(e1*e2)
                    if e2 != 0:
                        arr[i].add(e1//e2)
        if number in arr[i]:
            return i+1
        
    return -1
