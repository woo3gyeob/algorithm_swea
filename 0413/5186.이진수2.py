def binary(n, k):
    global answer
    if k > 12:
        return False
    if n < 2 ** -k:
        answer += '0'
        return binary(n, k + 1)
    else:
        n -= 2 ** -k
        answer += '1'
        if n == 0.0:
            return answer
        return binary(n, k + 1)


for tc in range(1, int(input()) + 1):
    n = float(input())
    answer = ''
    if not binary(n, 1):
        answer = 'overflow'
    print('#%d %s' % (tc, answer))
