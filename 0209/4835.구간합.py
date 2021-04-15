T = int(input())
answer = []
for test_n in range(1, T + 1):
    n, m = map(int, input().split())
    num_ls = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    for i in range(m):
        max_sum += num_ls[i]
        min_sum += num_ls[i]

    for i in range(1, n - m + 1):
        m_sum = 0
        for j in range(i, m + i):
            m_sum += num_ls[j]
        if m_sum > max_sum:
            max_sum = m_sum
        if m_sum < min_sum:
            min_sum = m_sum
    answer.append('#' + str(test_n) + ' ' + str(max_sum - min_sum) + '\n')
print(''.join(answer))