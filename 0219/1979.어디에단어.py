T = int(input())
answer = []
for tc in range(1, T+1):
    arr = []
    n, k = map(int, input().split())
    cnt = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        row += [0]
        i = 0
        while i < n:
            m = 1
            if row[i]:
                while row[i+m]:
                    m += 1
                if m == k:
                    cnt += 1
                i += m - 1
            i += 1
    arr.append([0]*n)
    for col in range(n):
        i = 0
        while i < n:
            m = 1
            if arr[i][col]:
                while arr[i+m][col]:
                    m += 1
                if m == k:
                    cnt += 1
                i += m - 1
            i += 1
    answer.append('#%d %d\n' %(tc, cnt))
print(''.join(answer))