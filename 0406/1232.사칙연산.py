def postorder(node):
    if len(tree[node]) > 2:
        cal, l, r = tree[node][1], postorder(int(tree[node][2])), postorder(int(tree[node][3]))
        if cal == '+':
            return l + r
        elif cal == '-':
            return l - r
        elif cal == '*':
            return l * r
        else:
            return l / r
    else:
        return int(tree[node][1])

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    for i in range(1, n+1):
        ls = input().split()
        tree[i] = ls
    print('#%d %d' %(tc, int(postorder(1))))