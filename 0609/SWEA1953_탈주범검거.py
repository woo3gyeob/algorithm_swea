from collections import deque

def find_criminal(sr, sc, time):
    visit = [[0]*m for _ in range(n)]
    visit[sr][sc] = 1
    arrivable_area = 1
    S = deque()
    S.append((sr, sc))
    while S:
        time -= 1
        for _ in range(len(S)):
            r, c = S.popleft()
            for d in directions[arr[r][c]]:
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
                if is_passable[d][arr[r][c]][arr[nr][nc]] and not visit[nr][nc]:
                    visit[nr][nc] = 1
                    arrivable_area += 1
                    S.append((nr,nc))
        
        if time == 1 or not S:
            return arrivable_area
        

dr = [0,1,0,-1]
dc = [1,0,-1,0]

directions = [
    [],
    [0,1,2,3],
    [1,3],
    [0,2],
    [0,3],
    [0,1],
    [1,2],
    [2,3]]

is_passable = [
    [[0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,1,1],
    [0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,1,1],
    [0,1,0,1,0,0,1,1],
    [0,1,0,1,0,0,1,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]],

    [[0,0,0,0,0,0,0,0],
    [0,1,1,0,1,0,0,1],
    [0,1,1,0,1,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,1,0,0,1],
    [0,1,1,0,1,0,0,1],
    [0,0,0,0,0,0,0,0]],

    [[0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,0],
    [0,1,0,1,1,1,0,0]],

    [[0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0]]]

for tc in range(1, int(input()) + 1):
    n, m, sr, sc, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    if time == 1:
        area = 1
    else:
        area = find_criminal(sr,sc, time)
    print('#%d %d' %(tc, area))
