# 다른 방법 , 시간초과 X

num = int(input())
root = int(num**0.5)
num_list = [i**2 for i in range(root+1)]
square_list = [i**2 + j**2 for i in range(root+1) for j in range(root+1)]

def decide(num):
    if num in num_list:
        return 1
    elif num in square_list:
        return 2
    else:
        for i in num_list:
            if num-i in square_list:
                return 3
        return 4
    
print(decide(num))
