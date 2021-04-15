T = int(input())
answer = []
for tc in range(1,T+1):
    n, k = map(int, input().split())
    cnt = 0
    for i in range((1<<n)-1, 1<<12):
        sum_val = 0
        ls = []
        for j in range(12):
            if i & (1<<j):
                ls.append(j+1)
        if len(ls) == n and sum(ls) == k:
            cnt += 1
    answer.append('#' + str(tc) + ' ' + str(cnt) + '\n')
print(''.join(answer))