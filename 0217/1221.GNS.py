T = int(input())
ls = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    num, N = input().split()
    n = list(input().split())
    cnt_ls = [0]*10
    for j in n:
        for i in range(10):
            if ls[i] == j:
                cnt_ls[i] += 1
                break
    print(f'#{tc}')
    for i in range(10):
        print((ls[i] + ' ') * cnt_ls[i], end = ' ')
    print()