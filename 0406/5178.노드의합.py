def postorder(node):
    if node <= n:
        postorder(node * 2)
        postorder(node * 2 + 1)
        tree[node // 2] += tree[node]


for tc in range(1, int(input()) + 1):
    n, m, L = map(int, input().split())
    tree = [0] * (n + 1)
    for i in range(m):
        j, val = map(int, input().split())
        tree[j] = val
    postorder(1)
    print('#%d %d' % (tc, tree[L]))