# 은근 쉬우면서 구현하기 까다로움 (시간 초과 고려해야함)
# deque 로 선언했고, 큐가 비어있는지 확인하기 위해 if q 이용
# 새롭게 함수를 구현해봄

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

def push(i):
    queue.append(i)
    
def pop(q):
    return q.popleft() if q else -1

def size(q):
    return len(q)

def empty(q):
    return 0 if q else 1

def front(q):
    return q[0] if q else -1

def back(q):
    return q[-1] if q else -1


for _ in range(n):
    string = input().rstrip()
    
    if string[:4] == "push":
        push(int(string[5:]))
    elif string == "pop":
        print(pop(queue))
    elif string == "size":
        print(size(queue))
    elif string == "empty":
        print(empty(queue))
    elif string == "front":
        print(front(queue))
    elif string == "back":
        print(back(queue))
    
