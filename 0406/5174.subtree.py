def inorder(node):
    global cnt
    for i in tree[node]:
        cnt += 1
        inorder(i)


for tc in range(1, int(input()) + 1):
    E, n = map(int, input().split())
    tree = [[] for _ in range(E + 2)]
    arr = list(map(int, input().split()))
    for i in range(0, 2 * E, 2):
        tree[arr[i]].append(arr[i + 1])
    cnt = 1
    inorder(n)
    print('#%d %d' % (tc, cnt))