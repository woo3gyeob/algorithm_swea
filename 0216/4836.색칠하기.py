T = int(input())
answer = []
for tc in range(1,T+1):
    n = int(input())
    ls1 = []
    ls2 = []
    cnt = 0
    for _ in range(n):
        lx, ly, rx, ry, color = map(int, input().split())
        if color == 1:
            for i in range(lx, rx + 1):
                for j in range(ly, ry + 1):
                    new = [i,j]
                    if new not in ls1:
                        ls1.append([i,j])
        else:
            for i in range(lx, rx + 1):
                for j in range(ly, ry + 1):
                    new = [i,j]
                    if new not in ls2:
                        ls2.append([i,j])
    for a in ls1:
        for b in ls2:
            if a == b:
                cnt += 1
                break
    answer.append('#' + str(tc) + ' ' + str(cnt) + '\n')
print(''.join(answer))