def push(item):
    global top
    top += 1
    S[top] = item


def pop():
    global top
    ret = S[top]
    top -= 1
    return ret


def is_empty():
    global top
    return top == -1


answer = []
for tc in range(1, 11):
    n = int(input())
    expression = input()
    S = [0] * n
    top = -1
    postfix = ''
    for i in expression:
        if i == '*':
            while not is_empty():
                j = pop()
                if j == '+':
                    push(j)
                    break
                postfix += j
            push(i)
        elif i == '+':
            while not is_empty():
                j = pop()
                postfix += j
            push(i)
        else:
            postfix += i
    while not is_empty():
        j = pop()
        postfix += j
    for i in postfix:
        if i in ['*', '+']:
            b = pop()
            a = pop()
            if i == '+':
                push(a + b)
            else:
                push(a * b)
        else:
            push(int(i))
    result = pop()
    answer.append('#%d %d\n' % (tc, result))
print(''.join(answer))