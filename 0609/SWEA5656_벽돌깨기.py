import copy
def dfs(idx,mapp2):
    global block_cnt
    if idx == N: # 종료 기준 = 슛팅횟수만큼 탐색
        cnt = 0
        for z in range(H): # 0을 세서 전체 리스트 요소 개수에서 빼주면 남은 벽돌 개수가 나옴
            cnt += mapp2[z].count(0)
        result_cnt = W*H - cnt
        if result_cnt < block_cnt:
            block_cnt = result_cnt
        return

    for y in range(W): # 구슬 쏘는 위치(열)
        check = 0
        for x in range(H): # 가장 위에 있는 벽돌을 찾음 (행)
            if not mapp2[x][y]: # 맵이 0이면 블록이 없다는 뜻이기에 다음 행 탐색
                continue
            else: 
                init_mapp = copy.deepcopy(mapp2) # 초기맵 복사 // 맵을 터뜨릴꺼기에 백트래킹 때 맵 복구를 위해서
                q = [(x,y,mapp2[x][y])] 
                while q: # BFS // 가능한 벽돌 다 터뜨림
                    qq = q.pop(0)
                    if qq[2] == 1: #블록숫자가 1이면 자기만 터짐
                        mapp2[qq[0]][qq[1]] = 0
                    else:
                        mapp2[qq[0]][qq[1]] = 0 
                        for k in range(1,qq[2]): # 블록 숫자 - 1만큼 연쇄폭발
                            for i in range(4):
                                if 0 <= qq[0]+dx[i]*k < H and 0 <= qq[1]+dy[i]*k < W and mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k] != 0:
                                    if (qq[0]+dx[i]*k,qq[1]+dy[i]*k,mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k]) not in q: # 큐에 중복으로 들어가는 것 방지                  
                                        q.append((qq[0]+dx[i]*k,qq[1]+dy[i]*k,mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k]))
            
                mapp3 = [[0 for _ in range(W)] for _ in range(H)]
                for j in range(W): # 벽돌 아래로 내리는 작업
                    temp = []
                    for i in range(H):
                        if mapp2[i][j]:
                            temp.append(mapp2[i][j])   
                    for a in range(len(temp)):
                        mapp3[H-len(temp)+a][j] = temp[a]
                check = 1 # 선택된 열에서 가장 높은 위치의 벽돌을 찾는 것이기에 행을 찾게 되면 그 다음 행을 탐색하면 안되기에 check를 통해 방지
            if check == 1: 
                dfs(idx+1,mapp3)
                mapp2 = init_mapp
                break
    dfs(N,mapp2) # 모든 행 열을 탐색해도 벽돌이 없다면 종료시킬 것임

T = int(input())
for t in range(T):
    N, W, H = map(int,input().split()) 
    mapp =[list(map(int,input().split())) for _ in range(H)]
    block_cnt = 999999999
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    dfs(0,mapp) 
    print('#{} {}'.format(t+1,block_cnt))
