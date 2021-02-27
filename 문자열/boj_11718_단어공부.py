string = input()

arr = [0]*26
maxx = -1    # 배열 내 가장 큰 수 저장

for s in string:
    if ord(s) > 90:    # 소문자
        arr[ord(s)-97] += 1
        maxx = max(arr[ord(s)-97], maxx)
    else:    # 대문자
        arr[ord(s)-65] += 1
        maxx = max(arr[ord(s)-65], maxx)

result = []
for i in range(26):     # 자꾸 string으로 범위 지정하는 실수 X -> index error
    if arr[i] == maxx:
        result.append(chr(i+65))    # 대문자로 저장
        
if len(result) > 1:
    print("?")
else:
    print(result[0])
