from collections import deque

def perm(x, cnt):
    S = deque()
    S.append((x, cnt))
    while S:
        for _ in range(len(S)):
            x, cnt = S.popleft()
            if check.get(x, 0): continue
            check[x] = 1
            if x == m:
                return cnt
            if 0 < x+1 <= 1000000:
                S.append((x+1, cnt+1))
            if x-1 > 0:
                S.append((x-1, cnt+1))
            if 0 < x*2 <= 1000000:
                S.append((x*2, cnt+1))
            if x-10 > 0:
                S.append((x-10, cnt+1))
        
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    check = {}
    min_cnt = perm(n, 0)
    print('#%d %d' %(tc, min_cnt))