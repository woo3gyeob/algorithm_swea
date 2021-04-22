def perm(node):
    for i in G[node]:
        if not visited[i]:
            visited[i] = 1
            perm(i)
    return

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(n+1)]
    for i in range(0, m*2-1, 2):
        G[arr[i]].append(arr[i+1])
        G[arr[i+1]].append(arr[i])
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            perm(i)
            cnt += 1
    print('#%d %d' %(tc, cnt))