def solution(brown, yellow):
    mid = int(yellow**(1/2))
    for i in range(1,mid+1):
        if yellow % i == 0:
            x = i
            y = yellow // i
            if ((4+x+y)*2) - 4 == brown:
                return [y+2,x+2]
            
