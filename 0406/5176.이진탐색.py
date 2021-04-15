def inorder(node):
    global cnt
    if node <= n:
        inorder(2*node)
        tree[node] = cnt
        cnt += 1
        inorder(2*node+1)

for tc in range(1, int(input())+1):
    n = int(input())
    tree = [0]*(n+1)
    cnt = 1
    inorder(1)
    print('#%d %d %d' %(tc, tree[1], tree[n//2]))