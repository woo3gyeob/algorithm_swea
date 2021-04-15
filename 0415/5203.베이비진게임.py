def is_triplet(idx, ls):
    for i in range(idx-1,1,-1):
        if ls[i] == ls[i-1] and ls[i-1] == ls[i-2]:
            return True
    return False

def is_run(idx, ls):
    ls = list(set(ls))
    n = len(ls)
    for i in range(n-1, 1, -1):
        if ls[i] - ls[i-1] == 1 and ls[i-1] - ls[i-2] == 1:
            return True
    return False

def babygin(idx):
    global winner
    if idx == 7:
        return
    x = sorted(a[:idx])
    y = sorted(b[:idx])
    if is_triplet(idx, x) or is_run(idx, x):
        winner = 1
        return
    elif is_triplet(idx, y) or is_run(idx, y):
        winner = 2
        return
    return babygin(idx+1)


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    a = [0]*6
    b = [0]*6
    k = 0
    for i in range(0,12,2):
        a[k] = arr[i]
        b[k] = arr[i+1]
        k += 1
    winner = 0
    babygin(3)
    print('#%d %d' %(tc, winner))