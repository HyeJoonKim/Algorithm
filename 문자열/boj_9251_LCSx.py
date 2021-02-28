first = input()
second = input()

arr = [[0] * (len(first)+1) for _ in range(len(second)+1)]

for i in range(len(second)):
    for j in range(len(first)):
        if second[i] == first[j]:
            arr[i+1][j+1] = arr[i][j] + 1
        else:
            arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])
            
print(arr[len(second)][len(first)])
