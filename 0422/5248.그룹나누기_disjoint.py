for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    
    # ---- disjoint set ------------------
    p = [i for i in range(V+1)]
    def findSet(x):
        if x != p[x]:
            p[x] = findSet(p[x])
        return p[x]
    
    # -------------------------------------
    arr = list(map(int, input().split()))
    ans = V
    for i in range(0, E*2, 2):
        a, b = findSet(arr[i]), findSet(arr[i+1])
        if a == b: continue
        p[b] = a # p[a] = b
        ans -= 1
    
    print('#%d %d' %(tc, ans))