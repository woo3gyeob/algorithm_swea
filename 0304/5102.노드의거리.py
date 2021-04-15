# pass
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    D = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, goal = map(int, input().split())
    S = [start]
    distance = 0
    while S:
        node = S.pop(0)
        if node == goal:
            distance = D[node]
            break
        for w in G[node]:
            if not D[w]:
                S.append(w)
                D[w] = D[node] + 1
    print('#%d %d' %(tc, distance))