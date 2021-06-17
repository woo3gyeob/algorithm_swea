def calc_height(x, y, z):
    global max_height
    flag = False
    for i in range(n):
        if visit[i]: continue
        visit[i] = 1
        a, b, c = boxes[i]
        if a <= x and b <= y:
            flag = True
            calc_height(a, b, z+c)
        elif a <= y and b <= x:
            flag = True
            calc_height(a, b, z+c)
        if a <= x and c <= y:
            flag = True
            calc_height(a, c, z+b)
        elif a <= y and c <= x:
            flag = True
            calc_height(a, c, z+b)
        if c <= x and b <= y:
            flag = True
            calc_height(c, b, z+a)
        elif c <= y and b <= x:
            flag = True
            calc_height(c, b, z+a)
        visit[i] = 0
    if not flag:
        if z > max_height:
            max_height = z

for tc in range(1, int(input()) + 1):
    n = int(input())
    boxes = [list(map(int, input().split())) for _ in range(n)]
    visit = [0]*n
    max_height = 0
    for i in range(n):
        visit[i] = 1
        a, b, c = boxes[i]
        calc_height(c, a, b)
        calc_height(b, a, c)
        calc_height(b, c, a)
        visit[i] = 0
    print('#%d %d' %(tc, max_height))