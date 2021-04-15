T = int(input())
answer = []
for tc in range(1, T+1):
    arr = []
    word = input()
    arr.append(word)
    max_len = len(word)
    len_ls = [max_len]
    for _ in range(4):
        word = input()
        arr.append(word)
        len_wd = len(word)
        len_ls.append(len_wd)
        if len_wd > max_len:
            max_len = len_wd
    words = ''
    for i in range(max_len):
        for j in range(5):
            if len_ls[j] > i:
                words += arr[j][i]
    answer.append('#%d %s\n' %(tc, words))
print(''.join(answer))