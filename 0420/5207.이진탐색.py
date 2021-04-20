def perm(s, e, flag):
    mid = (s + e) >> 1
    if s == e:
        if A[mid] == goal:
            return True
        return False

    if A[mid] == goal:
        return True

    elif A[mid] < goal:
        new_flag = True
        if flag ^ new_flag:
            if perm(mid + 1, e, new_flag): return True
    else:
        new_flag = False
        if flag ^ new_flag:
            if perm(s, mid - 1, new_flag): return True
    return False


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    j = (n - 1) >> 1
    for i in range(m):
        goal = B[i]
        if A[j] == goal:
            cnt += 1
        elif A[j] > goal:
            if perm(0, n - 1, True):
                cnt += 1
        else:
            if perm(0, n - 1, False):
                cnt += 1
    print('#%d %d' % (tc, cnt))