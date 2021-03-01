n = int(input())

stack = []
p = []
count = 1
flag = True

for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        p.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        p.append('-')
    else:
        flag = False
        
if flag == False:
    print('NO')
else:
    for i in p:
        print(i)
