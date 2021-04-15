import sys;

sys.stdin = open('1240.txt', 'r')

P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

arr = [[0] * 2000 for _ in range(2000)]  # 2진수로 변환해서 저장


def passCodeScan():
    ans = 0
    for i in range(n):
        j = m * 4 - 1
        while j >= 0:
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                code = []
                for _ in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 0:
                        j -= 1
                    while arr[i][j] == 1:
                        c4, j = c4 + 1, j - 1
                    while arr[i][j] == 0:
                        c3, j = c3 + 1, j - 1
                    while arr[i][j] == 1:
                        c2, j = c2 + 1, j - 1
                    min_val = min(c2, c3, c4)
                    code.append(P[(c2 // min_val, c3 // min_val, c4 // min_val)])

                a = code[0] + code[2] + code[4] + code[6]
                b = code[1] + code[3] + code[5] + code[7]
                if (b * 3 + a) % 10 == 0:
                    ans += a + b
            j -= 1
    return ans


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    for i in range(n):
        ls = input()
        tmp = []
        for j in range(m):
            val = int(ls[j], 16)
            arr[i][j * 4] = 1 if val & 8 else 0
            arr[i][j * 4 + 1] = 1 if val & 4 else 0
            arr[i][j * 4 + 2] = 1 if val & 2 else 0
            arr[i][j * 4 + 3] = 1 if val & 1 else 0
        arr.append(tmp)
    print('#{} {}'.format(tc, passCodeScan()))