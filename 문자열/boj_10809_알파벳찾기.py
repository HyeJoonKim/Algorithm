# 아스키 코드 외워야 유리
# 숫자 <-> 문자 변환 함수 기억하기
# 한 줄로 출력하는 방법 기억

S = input()

arr = [-1]*26
i = -1
for s in S:
    i += 1
    if arr[ord(s)-97] == -1:
        arr[ord(s)-97] = i
        
for i in range(26):
    print(arr[i], end=' ')
