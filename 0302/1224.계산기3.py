def push(item):
    global top
    top += 1
    stack[top] = item


def pop():
    global top
    ret = stack[top]
    top -= 1
    return ret


def is_empty():
    global top
    return top == -1


instack = {'(': 0, '+': 1, '*': 2}
incoming = {'(': 3, '+': 1, '*': 2}
answer = []
for tc in range(1, 11):
    n = int(input())
    s = input()
    top = -1
    stack = [0] * n
    postfix = ''
    for i in s:
        if i == '(':
            push(i)
        elif i in ['+', '*']:
            if not is_empty():
                while True:
                    if incoming[i] > instack[stack[top]]:
                        push(i)
                        break
                    else:
                        j = pop()
                        postfix += j
            else:
                push(i)
        elif i == ')':
            while stack[top] != '(':
                j = pop()
                postfix += j
            j = pop()
        else:
            postfix += i
    for i in postfix:
        if i == '+':
            b = pop()
            a = pop()
            push(a + b)
        elif i == '*':
            b = pop()
            a = pop()
            push(a * b)
        else:
            push(int(i))
    result = pop()
    answer.append('#%d %d\n' % (tc, result))
print(''.join(answer))