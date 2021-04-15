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

answer = []
for tc in range(1, int(input())+1):
    string = input()
    stack = [0] * len(string)
    top = -1
    cnt = 0
    push(string[0])
    for i in range(1, len(string)):
        if is_empty():
            push(string[i])
        else:
            item = pop()
            if item == string[i]:
                cnt += 1
            else:
                push(item)
                push(string[i])
    answer.append('#%d %d\n' %(tc, len(string) - cnt*2))
print(''.join(answer))