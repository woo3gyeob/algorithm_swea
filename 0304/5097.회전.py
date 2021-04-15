for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # n : 숫자 개수, m : 작업 수
    ls = list(map(int, input().split()))
    front, rear = 0, n - 1
    n = n % m
    for _ in range(m):
        front = (front + 1) % n
    print('#%d %d' % (tc, ls[front]))
