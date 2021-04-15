def inorder(node):
    global answer
    if 0 < node <= N:
        if visited[node] == False:
            inorder(node * 2)
            visited[node] = True
            answer += tree[node]
            inorder((node * 2) + 1)


for tc in range(1, 11):
    N = int(input())
    tree = [0]
    visited = [False] * (N + 1)
    answer = ''
    for _ in range(N):
        tree.append(input().split()[1])
    inorder(1)
    print('#%d %s' % (tc, answer))