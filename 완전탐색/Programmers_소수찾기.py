from itertools import permutations

def solution(numbers):
    l = []
    for i in range(1,len(numbers)+1):
        arr = set(permutations(numbers,i))  # 숫자 조합 만들기, 중복 빼기
        for j in arr:
            num = int(''.join(j))   # 숫자 만들기
            l.append(num)
    l = set(l)  # 숫자 리스트 중복 제거 
    
    result = 0  # 전체 소수 개수
    for j in l: # 숫자 리스트에 있는 각 숫자에 대하여
        cnt = 0
        if j == 1 or j == 0:
            continue
        mid = int(j**(1/2))+1  
        for k in range(2,mid):
            if j % k == 0:
                cnt += 1
        if cnt == 0:
            result += 1
    return result
