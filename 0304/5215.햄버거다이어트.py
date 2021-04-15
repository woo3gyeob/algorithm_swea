for tc in range(1, int(input()) + 1):
    n, L = map(int, input().split())
    lt, lc = [], []
    for i in range(n):
        t, k = map(int, input().split())
        lt.append(t)
        lc.append(k)
    max_taste = 0
    for i in range(1<<n):
        taste = 0
        cal = 0
        for j in range(n):
            if i & (1<<j):
                cal += lc[j]
                if cal > L:
                    break
                taste += lt[j]
        else:
            if max_taste < taste:
                max_taste = taste
    print('#%d %d' %(tc, max_taste))