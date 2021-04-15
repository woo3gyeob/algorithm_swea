def min_heap(idx):
    if idx <= n:
        tree[idx] = nums[idx-1]
        i = idx
        while tree[i] < tree[i//2]:
            tree[i//2], tree[i] = tree[i], tree[i//2]
            i = i // 2
        min_heap(idx+1)

for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [0]*(n+1)
    min_heap(1)
    sum_val = 0
    n = n // 2
    while n > 0:
        sum_val += tree[n]
        n = n // 2
    print('#%d %d' %(tc, sum_val))