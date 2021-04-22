from collections import deque

def bfs(r,c):
    S = deque()
    S.append((r,c))
    while S:
        r, c = S.popleft()
        for i in range(4):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            differ = max(arr[nr][nc] - arr[r][c], 0) + 1
            if D[r][c] + differ < D[nr][nc]:
                D[nr][nc] = D[r][c] + differ
                S.append((nr,nc))


delta = [(1,0),(0,1),(-1,0),(0,-1)]
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    D = [[0xfffff]*n for _ in range(n)]
    D[0][0] = 0
    bfs(0,0)
    print('#%d %d' %(tc, D[n-1][n-1]))