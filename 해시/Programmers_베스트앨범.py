# 딕셔너리 값 정렬에서 시간 많이 씀 ㅠ
# 정석대로는 for 구문도 {} 만들어서 사용해야 할듯

def solution(genres, plays):
    
    h = {}  #장르별 재생 횟수
    for g, p in zip(genres, plays):
        if not h.get(g):
            h[g] = p
        else:
            h[g] += p
    
    result = []
    h = sorted(h.items(), key=lambda x: -x[1])

    for i in h:
        arr = []
        for j in range(len(genres)):
            if genres[j] == i[0]:
                arr.append((plays[j],j))
        arr.sort(key = lambda x: (-x[0], x[1]))
        if len(arr) == 1:
            result.append(arr[0][1])
        else:
            result.append(arr[0][1])
            result.append(arr[1][1])
    return result
