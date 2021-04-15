dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c):
    global flag, len_r, len_c
    if arr[r][c] != 0:
        arr[r][c] = 0
        flag = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < n and nr > -1 and nc < n and nc > -1:
                if arr[nr][nc] != 0:
                    if nr > len_r:
                        len_r = nr
                    if nc > len_c:
                        len_c = nc
                    dfs(nr, nc)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    result = []
    for i in range(n):
        for j in range(n):
            flag, len_r, len_c = False, i, j
            dfs(i, j)
            if flag:
                cnt += 1
                result.append((len_r - i + 1, len_c - j + 1))

    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            if result[i][0] * result[i][1] > result[j][0] * result[j][1]:
                result[i], result[j] = result[j], result[i]
            elif result[i][0] * result[i][1] == result[j][0] * result[j][1]:
                if result[i][0] > result[j][0]:
                    result[i], result[j] = result[j], result[i]
    print('#%d %d' % (tc, cnt), end=' ')
    for i in range(len(result)):
        print(*result[i], end=' ')
    print()