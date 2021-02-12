K = int(input())

arrA = [0]*(K+1)
arrB = [0]*(K+1)
arrA[0] = 1
arrB[1] = 1

for i in range(2,K+1):
    arrA[i] = arrA[i-1] + arrA[i-2]
    arrB[i] = arrB[i-1] + arrB[i-2]
    
print(arrA[K],arrB[K])
