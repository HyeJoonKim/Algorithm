n = int(input())

for i in range(n):
    result = input()
    o = 0
    score = 0
    for j in range(len(result)):
        if result[j] == 'X':
            o =0
        else:
            o += 1
            score += o
    print(score)
