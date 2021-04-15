def dfs(v):
    visit[v] = 1
    for w in G[v]:
        if visit[w] == 0:
            dfs(w)

for _ in range(10):
    tc, V = map(int, input().split())
    line = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    visit = [0] * 100
    for i in range(0, V*2, 2):
        u, v = line[i], line[i+1]
        G[u].append(v)
    dfs(0)
    print('#%d %d' %(tc, visit[99]))