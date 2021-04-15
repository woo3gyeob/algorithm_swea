def find_min_index(heights):
    for i in range(99, 0, -1):
        if heights[i] < heights[i-1]:
            return i
def find_max_index(heights):
    for i in range(99):
        if heights[i] > heights[i+1]:
            return i
answer = []
for test_case_num in range(1,11):
    dump = int(input())
    heights = list(map(int, input().split()))
    for i in range(99, -1, -1):
        for j in range(i):
            if heights[j] < heights[j+1]:
                heights[j], heights[j+1] = heights[j+1], heights[j]
    for i in range(dump):
        max_index = find_max_index(heights)
        min_index = find_min_index(heights)
        if max_index is None:
            answer.append('#'+str(test_case_num)+' '+str(0)+'\n')
            break
        elif min_index - max_index == 1:
            answer.append('#'+str(test_case_num)+' '+str(0)+'\n')
            break
        else:
            heights[max_index] -= 1
            heights[min_index] += 1
            if i == (dump-1):
                answer.append('#'+str(test_case_num)+' '+str(heights[0] - heights[99])+'\n')
print(''.join(answer))