answer = []
for _ in range(10):
    tc = int(input())
    arr = [(list(map(int, input().split()))) for _ in range(100)]
    for i in range(100):
        if arr[0][i] == 1:
            x = i * 1
            y = 1
            while y <= 98:
                flag = False
                if x != 0:
                    while arr[y][x-1] == 1:
                        flag = True
                        if x == 0:
                            break
                        x -= 1
                if x != 99 and flag == False:
                    while arr[y][x+1] == 1:
                        if x == 98:
                            x += 1
                            break
                        x += 1
                y += 1
            if arr[y][x] == 2:
                answer.append('#' + str(tc) + ' ' + str(i) + '\n')
                break
print(''.join(answer))