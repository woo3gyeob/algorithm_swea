def game(start, end):
    if start == end:
        return start

    a = game(start, (start + end) // 2)
    b = game((start + end) // 2 + 1, end)

    if (ls[b] == 1 and ls[a] == 3) or (ls[b] == 2 and ls[a] == 1) or (ls[b] == 3 and ls[a] == 2):
        return b
    else:
        return a


answer = []
for tc in range(1, int(input()) + 1):
    n = int(input())
    ls = [0] + list(map(int, input().split()))
    winner = game(1, n)
    answer.append('#%d %d\n' % (tc, winner))
print(''.join(answer))