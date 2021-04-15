T = int(input())
answer = []
for tc in range(1, T+1):
    short = input()
    long = input()
    is_same = 0
    for i in range(len(long) - len(short) + 1):
        if long[i:i + len(short)] == short:
            is_same = 1
    answer.append('#%d %d\n' %(tc, is_same))
print(''.join(answer))