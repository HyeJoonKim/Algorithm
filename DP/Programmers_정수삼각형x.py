# 한 줄씩 더해가는 것 생각 못함
# 더해서 다른 리스트에 저장해야 하는 것에 집중해서ㅠ

def solution(triangle):
    for i in range(len(triangle)-1):
        triangle[i+1][0] = triangle[i][0] + triangle[i+1][0]
        triangle[i+1][-1] = triangle[i][-1] + triangle[i+1][-1]
    
    for j in range(1,len(triangle)-1):
        for k in range(1,len(triangle[j])):
            triangle[j+1][k] += max(triangle[j][k-1], triangle[j][k])
    
    return max(triangle[-1])
