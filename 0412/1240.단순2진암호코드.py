dic = {'0001101':0,
      '0011001':1,
      '0010011':2,
      '0111101':3,
      '0100011':4,
      '0110001':5,
      '0101111':6,
      '0111011':7,
      '0110111':8,
      '0001011':9}
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                r, c = i, j - 55
                break
    ls = [0]*8
    idx = 0
    for i in range(c, c + 7*7+1, 7):
        ls[idx] = dic[arr[r][i:i+7]]
        idx += 1
         
    sum_val = 0
    for i in range(8):
        if i % 2:
            sum_val += ls[i]
        else:
            sum_val += ls[i]*3
    answer = sum(ls) if sum_val % 10 == 0 else 0
    print('#%d %d' %(tc, answer))