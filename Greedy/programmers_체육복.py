def solution(n, lost, reserve):
    student = [1] * (n+1)
    answer = 0
    
    for i in range(1,n+1):
        if i in lost:
            student[i] -= 1
        if i in reserve:
            student[i] += 1
            
    for i in range(1, n+1):
        if student[i] == 0:
            if student[i-1] > 1 and i > 1:
                student[i] = 1
                student[i-1] -= 1
                answer += 1
                continue
            elif i < n and student[i+1] > 1:
                student[i] = 1
                student[i+1] -= 1
                answer += 1
                continue
        else:
            answer += 1

    return answer
