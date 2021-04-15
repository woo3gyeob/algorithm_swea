def pascal(k, arr):
    if k == n + 1:
        return arr
    else:
        ls = []
        ls.append(1)
        for i in range(1, k - 1):
            ls.append(arr[k - 2][i - 1] + arr[k - 2][i])
        ls.append(1)
        arr.append(ls)
        return pascal(k + 1, arr)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    pas = [[1], [1, 1]]
    if n >= 3:
        pas = pascal(3, pas)
    print('#%d' % tc)
    print('1')
    for i in range(1, n):
        print(' '.join(list(map(str, pas[i]))))