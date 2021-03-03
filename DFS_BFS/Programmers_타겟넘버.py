result = 0

def dfs(idx,numbers,target,total):
    global result
    if len(numbers) == idx and total == target:
        result += 1
        return
    if len(numbers) == idx:
        return
            
    dfs(idx+1,numbers,target,total+numbers[idx])
    dfs(idx+1,numbers,target,total-numbers[idx])



def solution(numbers, target):
    global result
    dfs(0,numbers,target,0)
    return result
