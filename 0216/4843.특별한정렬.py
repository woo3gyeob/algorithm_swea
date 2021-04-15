def selectionsort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

T = int(input())
answer = []
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = selectionsort(arr)
    nums = []
    for i in range(10):
        if i % 2:
            nums.append(arr[n - (i//2)-1])
        else:
            nums.append(arr[i//2])
    answer.append('#' + str(tc) + ' ' + ' '.join(list(map(str, nums))) + '\n')
print(''.join(answer))