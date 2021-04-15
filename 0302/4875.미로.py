dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def DFS(r, c):
    global flag
    if arr[r][c] == 3:
        flag = 1
        return
    arr[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
            continue
        if arr[nr][nc] == 0 or arr[nr][nc] == 3:
            DFS(nr, nc)


answer = []
for tc in range(1, int(input()) + 1):
    flag = 0
    n = int(input())
    arr = []
    for i in range(n):
        ls = list(map(int, list(input())))
        for j in range(n):
            if ls[j] == 2:
                sr, sc = i, j
        arr.append(ls)
    DFS(sr, sc)
    answer.append('#%d %d\n' % (tc, flag))
print(''.join(answer))