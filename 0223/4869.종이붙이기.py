def paper(x):
    if x == n:
        return 1
    if x > n:
        return 0
    return paper(x+10) + paper(x+20) * 2

T = int(input())
answer = []
for tc in range(1, T + 1):
    n = int(input())
    answer.append('#%d %d\n' %(tc, paper(0)))
print(''.join(answer))

'''
# 시간제한 걸린 코드
def paper(i, n):
    if i == n:
        global cnt
        cnt += 1
    else:
        if n - i == 10:
            paper(i+10, n)
        else:
            paper(i+10, n)
            paper(i+20, n)
            paper(i+20, n)
T = int(input())
answer = []
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    paper(0,n)
    answer.append('#%d %d\n' %(tc, cnt))
print(''.join(answer))
'''