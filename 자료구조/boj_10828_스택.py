# rstrip() 필수

import sys
input = sys.stdin.readline
n = int(input())

stack = []

for _ in range(n):
    string = input().rstrip()
    
    if string[:4] == "push":
        stack.append(int(string[5:]))
        
    elif string == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif string == "size":
        print(len(stack))
        
    elif string == "empty":
        if not stack:
            print(1)
        else:
            print(0)
            
    elif string == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])   
            
