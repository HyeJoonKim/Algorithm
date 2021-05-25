def solution(number, k):
    arr = [number[0]]    
    
    for i in number[1:]:
        while k > 0 and len(arr) > 0 and arr[-1] < i :
            k -= 1
            arr.pop(-1)
        arr.append(i)
        
    if k > 0:
        k = len(arr)-k
        arr = arr[:k]
        
    return ''.join(arr)
            
