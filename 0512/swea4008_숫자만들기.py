# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def dfs(idx, num):
    global min_val, max_val
    if idx == n:
        if num < min_val:
            min_val = num
            
        if num > max_val:
            max_val = num
            
        return
    if operator[0]:
        operator[0] -= 1
        dfs(idx+1, num+arr[idx])
        operator[0] += 1
    if operator[1]:
        operator[1] -= 1
        dfs(idx+1, num-arr[idx])
        operator[1] += 1
    if operator[2]:
        operator[2] -= 1
        dfs(idx+1, num*arr[idx])
        operator[2] += 1
    if operator[3]:
        operator[3] -= 1
        dfs(idx+1, int(num/arr[idx]))
        operator[3] += 1

for tc in range(1, int(input())+1):
    n = int(input())
    n = int(input())
    operator = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    min_val = 0xffffffff
    max_val = -0xffffffff
    dfs(1, arr[0])
    print('%d %d' %(tc, max_val - min_val))