# 앞, 뒤 공백 제외한 공백 수 + 1 = 단어수
string = input()

total = 0
for i in string:
    if i == " ":
        total += 1    #전체 공백 수 계산
        
if string[0] == " ":
    total -= 1    #공백으로 시작하면 -1

if string[-1] == " ":
    total -= 1    # 공백으로 끝나면 -1
    
print(total + 1)    # 전체 공백 개수 + 1 = 단어수
