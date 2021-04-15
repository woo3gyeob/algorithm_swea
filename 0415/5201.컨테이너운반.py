def load():
    sum_val = 0
    idx = 0
    for i in range(n):
        if w[i] <= t[idx]:
            sum_val += w[i]
            idx += 1
            if idx > m - 1:
                break
    return sum_val


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    print('#%d %d' % (tc, load()))
