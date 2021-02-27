n = int(input())

for _ in range(n):
    ps = input()
    left = 0
    right = 0
    for i in ps:
        if i == '(':
            left += 1
        else:
            right += 1
        if left < right:
            print("NO")
            break
    if left == right:
        print("YES")
    elif left > right:
        print("NO")
