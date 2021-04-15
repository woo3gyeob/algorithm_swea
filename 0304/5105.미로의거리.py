dr = [1,0,-1,0]
dc = [0,1,0,-1]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = []
    for i in range(n):
        ls = list(map(int, list(input())))
        for j in range(n):
            if ls[j] == 2:
                sr, sc = i, j
            if ls[j] == 3:
                er, ec = i, j
        arr.append(ls)
    S = [(sr, sc)]
    D = [[0]*n for _ in range(n)]
    distance = 0
    while S:
        p = S.pop(0)
        r, c = p[0], p[1]
        arr[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < n and nr > -1 and nc < n and nc > -1:
                if arr[nr][nc] == 3:
                    distance = D[r][c]
                    break
                if arr[nr][nc] == 0:
                    D[nr][nc] = D[r][c] + 1
                    S.append((nr,nc))
    print('#%d %d' %(tc, distance))