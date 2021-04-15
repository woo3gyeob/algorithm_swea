dr = [0,1,0,-1]
dc = [1,0,-1,0]
for _ in range(10):
    arr = []
    tc = int(input())
    for i in range(16):
        ls = list(map(int, list(input())))
        for j in range(16):
            if ls[j] == 3:
                er, ec = i, j
        arr.append(ls)
    S = []
    S.append((1,1))
    result = 0
    while S:
        point = S.pop(0)
        arr[point[0]][point[1]] = 1
        if point == (er, ec):
            result = 1
            break
        for i in range(4):
            nr = point[0] + dr[i]
            nc = point[1] + dc[i]
            if arr[nr][nc] == 0 or arr[nr][nc] == 3:
                S.append((nr,nc))
    print('#%d %d' %(tc, result))