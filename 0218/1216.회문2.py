answer = []
for _ in range(10):
    tc = int(input())
    arr = []
    max_len = 1
    for _ in range(100):
        string = input()
        arr.append(string)
    for fixed_ax in range(100):
        flag = False
        for m in range(99, 1, -1):
            if flag:
                break
            else:
                for i in range(100 - m + 1):
                    for j in range(i, i + m//2):
                        if arr[j][fixed_ax] != arr[i + m - (j - i + 1)][fixed_ax]:
                            break
                    else:
                        if m > max_len:
                            max_len = m
                        flag = True
                    for j in range(i, i + m//2):
                        if arr[fixed_ax][j] != arr[fixed_ax][i + m - (j - i + 1)]:
                            break
                    else:
                        if m > max_len:
                            max_len = m
                        flag = True
    answer.append('#%d %d\n' %(tc, max_len))
print(''.join(answer))