T = int(input())
answer = []
for test_n in range(1, T+1):
    N = int(input())
    num_ls = list(map(int, input()))
    for i in range(len(num_ls)-1, -1, -1):
        for j in range(i):
            if num_ls[j] < num_ls[j+1]:
                num_ls[j], num_ls[j+1] = num_ls[j+1], num_ls[j]
    max_val = 0
    max_cnt = 0
    idx = 0
    for i in range(1, len(num_ls)):
        if num_ls[i-1] != num_ls[i]:
            cnt = i - idx
            idx = i
            if cnt > max_cnt:
                max_val = num_ls[i-1]
                max_cnt = cnt
        if i == (len(num_ls)-1):
            cnt = i - idx + 1
            if cnt > max_cnt:
                max_val = num_ls[i]
                max_cnt = cnt
    answer.append('#'+str(test_n)+' '+str(max_val)+' '+str(max_cnt)+'\n')
print(''.join(answer))