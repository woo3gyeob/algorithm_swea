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
    return top < -1

answer = []
for tc in range(1, int(input()) + 1):
    expression = list(input().split())
    stack = [0] * len(expression)
    top = -1
    result = ''
    for i in expression:
        if i in ['+','*','-','/']:
            b = pop()
            a = pop()
            if is_empty():
                result = 'error'
            else:
                if i == '+':
                    push(a+b)
                elif i == '*':
                    push(a*b)
                elif i == '-':
                    push(a-b)
                else:
                    push(int(a/b))
        elif i == '.':
            result = pop()
            if top != -1:
                result = 'error'
        else:
            push(int(i))
        if result == 'error':
            break
    print('#%d' %tc, end = ' ')
    print(result)