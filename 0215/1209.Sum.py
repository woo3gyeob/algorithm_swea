def find_max(*args):
    max_value = args[0]
    for i in range(1,len(args)):
        if args[i] > max_value:
            max_value = args[i]
    return max_value

answer = []
for _ in range(10):
    tc = int(input())
    arr = []
    max_val = 0
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    val_s, val_bs = 0, 0
    for i in range(100):
        val_s += arr[i][i]
        val_bs += arr[i][-i-1]
        val_r, val_c = 0, 0
        for j in range(100):
            val_r += arr[i][j]
            val_c += arr[j][i]
        max_val = find_max(max_val, val_c, val_r)
    max_val = find_max(max_val, val_s, val_bs)
    answer.append('#' + str(tc) + ' ' + str(max_val) + '\n')
print(''.join(answer))