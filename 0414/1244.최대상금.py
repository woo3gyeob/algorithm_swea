import sys;
sys.stdin = open('input8.txt', 'r')

def perm(idx):
    global max_cost
    if idx == exchange:
        cost = ''.join(arr)
        if max_cost < cost:
            max_cost = cost
        return
    for i in range(n):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            tmp = ''.join(arr)
            if not visit.get((tmp,idx+1)):
                visit[(tmp,idx+1)] = 1
                perm(idx+1)
            arr[i], arr[j] = arr[j], arr[i]

for tc in range(1, int(input())+1):
    arr, exchange = input().split()
    n = len(arr)
    exchange = int(exchange)
    arr = list(arr)
    max_cost = '0'
    visit = {}
    perm(0)
    print('#%d %s' %(tc, max_cost))