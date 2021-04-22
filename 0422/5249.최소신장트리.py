# 프림 알고리즘
# key : 가중치
# pi : 부모정점
# mst : 트리에 포함 여부

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append([v,w])
        G[v].append([u,w])
        
    key = [0xffffff] * (V+1)
    pi = [0] * (V+1)
    mst = [0] * (V+1)
    
    key[0] = 0
    ans = 0
    for _ in range(V+1):
        # key(가중치) 값이 최소인 정점을 선택
        u, minKey = 0, 0xffffff
        for i in range(V+1):
            if not mst[i] and minKey > key[i]: # 트리에 포함되지 않은 애만 조회
                u, minKey = i, key[i]
        mst[u] = 1
        ans += key[u]
        for v, w in G[u]:
            if not mst[v] and key[v] > w: # 아직 트리에 포함되지 않으면서 key값을 변경시켜줌
                key[v] = w
                pi[v] = u
    print('#%d %d' %(tc, ans))