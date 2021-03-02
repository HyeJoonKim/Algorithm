# 다양한 풀이들이 많으니 참고해보자

def solution(participant, completion):
    
    h = {}
    for p in participant:
        if not h.get(p):
            h[p] = 1
        else:
            h[p] += 1
        
    for c in completion:
        h[c] = h.get(c) - 1
        if h.get(c) == 0:
            del h[c]
        
    return(list(h.keys())[0])
