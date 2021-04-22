from collections import deque

def search(node):
    S = deque()
    S.append(node)
    while S:
        node = S.popleft()
        for u, w in G[node]:
            if D[node] + w < D[u]:
                D[u] = D[node] + w
                S.append(u)
    

for tc in range(1, int(input()) + 1):
    n, E = map(int, input().split())
    G = [[] for _ in range(n+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append([v,w])
    D = [0xffffff]*(n+1)
    D[0] = 0
    search(0)
    print('#%d %d' %(tc, D[n]))