for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    chz = list(map(int, input().split()))
    p = chz[:n]
    p_num = list(range(1, n+1))
    front = n
    while front < m:
        for i in range(n):
            p[i] = p[i]//2
            if p[i] == 0 and front < m:
                p[i] = chz[front]
                p_num[i] = front + 1
                front += 1
    while sum(p[i] <= 1 for i in range(n)) != n:
        for i in range(n):
            p[i] = p[i]//2
    for i in range(n-1,-1,-1):
        if p[i] == 1:
            last = p_num[i]
            break
    print('#%d %d' %(tc, last))