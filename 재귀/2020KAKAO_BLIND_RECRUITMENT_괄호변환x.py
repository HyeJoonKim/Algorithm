def check(string):
    left = 0    # (
    right = 0   # )     
    for i in string:
        if left < right:
            return 0
        if i == '(':
            left += 1
        else:
            right += 1
    return 1


def UV(string): # u,v 리턴
    left = 0
    right = 0
    u = ''
    for i in string:
        if i == '(':
            left += 1
        else:
            right += 1
        u += i
        if left == right:
            return u, string.replace(u,'',1)    
        
    
def reverse(u):
    answer = ''
    for i in range(1, len(u)-1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
    return answer

    
def recursive(string):
    if string == '':
        return ''
    u, v = UV(string)
    if check(u):
        return u + recursive(v)
    else:
        return '('+recursive(v)+')'+reverse(u)
    

def solution(p):
    return p if check(p) else recursive(p)
