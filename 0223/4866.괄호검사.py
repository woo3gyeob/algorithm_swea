def pop():
    global top
    ret = S[top]
    top -= 1
    return ret

def push(item):
    global top
    top += 1
    S[top] = item

def is_empty():
    global top
    return top == -1

T = int(input())
answer = []
for tc in range(1, T+1):
    string = input()
    top = -1
    S = [0]*len(string)
    is_pair = 1
    for i in string:
        if i in ['(','{']:
            push(i)
        if i in [')','}']:
            if is_empty():
                is_pair = 0
                break
            item = pop()
            if i == ')':
                if item != '(':
                    is_pair = 0
                    break
            else:
                if item != '{':
                    is_pair = 0
                    break
    if not is_empty():
        is_pair = 0
    answer.append('#%d %d\n' %(tc, is_pair))
print(''.join(answer))