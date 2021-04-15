def bin_search(l, r, target):
    c = int((l + r) / 2)
    if c == target:
        return 1
    if c < target:
        return 1 + bin_search(c, r, target)
    else:
        return 1 + bin_search(l, c, target)


T = int(input())
answer = []
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    cnt_a = bin_search(1, p, a)
    cnt_b = bin_search(1, p, b)
    if cnt_a > cnt_b:
        answer.append('#' + str(tc) + ' ' + 'B' + '\n')
    elif cnt_a < cnt_b:
        answer.append('#' + str(tc) + ' ' + 'A' + '\n')
    else:
        answer.append('#' + str(tc) + ' ' + str(0) + '\n')
print(''.join(answer))