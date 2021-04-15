T = int(input())
answer = []
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    min_val, max_val = nums[0], nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    answer.append('#' + str(i + 1) + ' ' + str(max_val - min_val) + '\n')
print(''.join(answer))
