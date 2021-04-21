def perm(idx, percent):
    global max_percent
    if percent <= max_percent:
        return
    if idx == n:
        max_percent = percent
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(idx+1, percent * arr[idx][i] / 100)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_percent = 0
    perm(0, 1)
    print('#%d %.6f' %(tc, max_percent*100))