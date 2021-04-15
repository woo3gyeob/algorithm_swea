def dfs(v):
    if v == g:
        return 1
    visit[v] = 1
    for w in G[v]:
        if visit[w] == 0:
            if dfs(w) == 1:
                return 1
    return 0


T = int(input())
answer = []
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    s, g = map(int, input().split())
    visit = [0] * (V + 1)
    is_path = dfs(s)
    answer.append('#%d %d\n' % (tc, is_path))
print(''.join(answer))