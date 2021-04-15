def perm(idx):
    global val, min_val
    if val > min_val:
        return
    if idx == n:
        if val < min_val:
            min_val = val
    else:
        for i in range(n):
            if check[i] == 0:
                val += arr[idx][i]
                check[i] = 1
                perm(idx + 1)
                check[i] = 0
                val -= arr[idx][i]

answer = []
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        ls = list(map(int, input().split()))
        arr.append(ls)
    val = 0
    check = [0] * n
    min_val = 100000000
    perm(0)
    answer.append('#%d %d\n' %(tc, min_val))
print(''.join(answer))