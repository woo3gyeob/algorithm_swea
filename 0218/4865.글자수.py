T = int(input())
answer = []
for tc in range(1, T+1):
    short = set(input())
    long = input()
    max_cnt = 0
    for i in short:
        cnt = 0
        for j in long:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    answer.append('#%d %d\n' %(tc, max_cnt))
print(''.join(answer))