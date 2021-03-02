def solution(clothes):    
    h = {}
    
    for i in clothes:
        if not h.get(i[1]):
            h[i[1]] = 1
        else:
            h[i[1]] += 1
            
    arr = list(h.values())
    result = 1
    for i in arr:
        result *= (i+1)
    return result - 1
