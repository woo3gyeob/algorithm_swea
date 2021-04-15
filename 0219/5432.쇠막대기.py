T = int(input())
answer = []
for tc in range(1, T+1):
    batch = input()
    stick = cnt = 0
    for i in range(len(batch)):
        if batch[i] == '(':
            stick += 1
        else:
            stick -= 1
            if batch[i-1] == '(':
                cnt += stick
            else:
                cnt += 1
    answer.append('#%d %d\n' %(tc, cnt))
print(''.join(answer))