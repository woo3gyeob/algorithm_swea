from collections import deque

def pinball(r, c, d):
    sr, sc = r, c
    point = 0
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if sr == nr and sc == nc: return point
        # 경계 벗어나면
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            point += 1
            d = (d+2) % 4
            r = nr
            c = nc
        elif arr[nr][nc] == 0:
            r = nr
            c = nc
        elif arr[nr][nc] == -1:
            return point
        elif arr[nr][nc] >= 1 and arr[nr][nc] <= 5: # 벽 만남
            d = reflected_direction[arr[nr][nc]][d]
            point += 1
            r = nr
            c = nc
        elif arr[nr][nc] >= 6 and arr[nr][nc] <= 10:
            r, c = wormholes[(nr,nc)]
    # 0 1 2 3
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 벽 종류(1~5)와 방향에 따른 튕겨져 나갈 방향
# 행 : 벽 번호, 동남서북 (d=0~3)
reflected_direction = [
    [],
    [2,0,3,1],
    [2,3,1,0],
    [1,3,0,2],
    [3,2,0,1],
    [2,3,0,1]]

for tc in range(1, int(input()) + 1):
    n = int(input())
    S = deque()
    arr = []
    wormholes = {}
    tmp = [list() for _ in range(11)]
    for i in range(n):
        ls = list(map(int, input().split()))
        for j in range(n):
            if ls[j] == 0:
                S.append((i,j))
            elif ls[j] >= 6 and ls[j] <= 10:
                tmp[ls[j]].append((i,j))
        arr.append(ls)

    # 웜홀 빠져나갈 좌표 ex_(0,0) -> (2,2)
    for i in range(6,11):
        if tmp[i]:
            wormholes[tmp[i][0]] = tmp[i][1]
            wormholes[tmp[i][1]] = tmp[i][0]

    max_point = 0
    for i in range(len(S)):
        for d in range(4):
            new_point = pinball(S[i][0], S[i][1] ,d)
            if new_point > max_point:
                max_point = new_point

    print('#%d %d' %(tc, max_point))

            