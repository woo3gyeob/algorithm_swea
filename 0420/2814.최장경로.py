def perm(node, d):
    global max_distance
    flag = False
    for i in G[node]:
        if not visited[i]:
            flag = True
            visited[i] = 1
            perm(i, d + 1)
            visited[i] = 0

    if not flag:
        if d > max_distance:
            max_distance = d
        return


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    max_distance = 0
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        visited[i] = 1
        perm(i, 1)
    print('#%d %d' % (tc, max_distance))