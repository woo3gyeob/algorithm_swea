for _ in range(10):
    tc = int(input())
    cQ = list(map(int, input().split()))
    front, rear, i = 0, 7, 0
    while True:
        cQ[front] -= (i % 5) + 1
        front = (front + 1) % 8
        rear = (rear + 1) % 8
        if cQ[rear] <= 0:
            cQ[rear] = 0
            break
        i += 1
    print('#%d' %tc, end=' ')
    print(*(cQ[front:] + cQ[:rear + 1]))
