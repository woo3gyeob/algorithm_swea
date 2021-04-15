T = int(input())
for tc in range(1,T+1):
    n = int(input())
    pas = [[1]]
    print('#%d' %tc)
    print('1')
    for i in range(1, n):
        ls = [0] + pas[i-1] + [0]
        ls2 = []
        for j in range(i+1):
            ls2.append(ls[j] + ls[j+1])
        pas.append(ls2)
        print(' '.join(list(map(str, ls2))))