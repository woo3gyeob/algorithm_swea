def dfs(r,c,cut,k):
    global max_distance
    flag = False        # 한번이라도 delta 이동 했으면 True로 바뀜
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < n and nc > -1 and nc < n:
            if not visited[nr][nc]:
                if arr[nr][nc] < arr[r][c]:     # 높이가 더 낮으면 바로 ㄱㄱ
                    flag = True
                    visited[nr][nc] = visited[r][c] + 1
                    dfs(nr,nc,cut,k)
                    visited[nr][nc] = 0
                elif not cut and arr[nr][nc] - k < arr[r][c]: # 아직 안깎았는데 깎을 수 있을 때
                    val = arr[nr][nc]           # 원래 높이 저장
                    arr[nr][nc] = arr[r][c] - 1 # 옆에꺼보다 1 낮게 높이 바꿈
                    flag = True
                    visited[nr][nc] = visited[r][c] + 1
                    dfs(nr,nc,True,0)
                    arr[nr][nc] = val           # dfs돌고 원래 높이 다시 할당
                    visited[nr][nc] = 0
    if not flag:    # 네군데 다 탐색해도 갈 수 없는 경우
        if max_distance < visited[r][c]:
            max_distance = visited[r][c]


dr = [1,0,-1,0]
dc = [0,1,0,-1]
for tc in range(1, int(input()) + 1):
    n ,k = map(int, input().split())
    arr = []
    max_height = 0
    for _ in range(n):
        ls = list(map(int, input().split()))
        arr.append(ls)
        h = max(ls)
        if max_height < h:  # 최대 높이 찾기
            max_height = h
    
    max_distance = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_height: # 최대 높이인 경우에 dfs 탐색
                visited[i][j] = 1
                dfs(i, j, False, k)     # 행, 열, 깎았는지여부, 깎을 수 있는 값
                visited[i][j] = 0
    print('#%d %d' %(tc, max_distance))