# 4012. [모의 SW 역량테스트] 요리사

def perm(idx, start):
    global min_difference
    if idx == n // 2:
        B_list = list(ls - set(sel))
        d = abs(calc_taste(sel) - calc_taste(B_list))
        if d < min_difference:
            min_difference = d
        return
    for i in range(start, n):
        sel[idx] = i
        perm(idx+1, i+1)

def calc_taste(foods):
    l = len(foods)
    taste = 0
    for i in range(l-1):
        for j in range(i+1, l):
            taste += arr[foods[i]][foods[j]] + arr[foods[j]][foods[i]]
    return taste

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    comb = []
    sel = [0] * (n//2)
    min_difference = 0xffffff
    ls = set(range(0,n))
    perm(0,0)
    print('#%d %d' %(tc, min_difference))