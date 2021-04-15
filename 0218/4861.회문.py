T = int(input())
answer = []
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = []
    pelindrom = None
    for _ in range(n):
        string = input()
        for i in range(n - m + 1):
            for j in range(i, i + m//2):
                if string[j] != string[i + m - (j - i + 1)]:
                    break
            else:
                pelindrom = string[i : i + m]
                break
        arr.append(string)
    if pelindrom is None:
        for col in range(n):
            for i in range(n - m + 1):
                for j in range(i, i + m//2):
                    if arr[j][col] != arr[i + m - (j - i + 1)][col]:
                        break
                else:
                    pelindrom = ''.join([arr[p][col] for p in range(i, i + m)])
                    break
    answer.append('#%d %s\n' %(tc, pelindrom))
print(''.join(answer))