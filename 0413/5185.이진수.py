for tc in range(1, int(input())+1):
    n, string = input().split()
    answer = ''
    for i in range(int(n)):
        integer = int(string[i], 16)
        binary = bin(integer)
        binary = binary[2:]
        binary = '0'*(4-len(binary)) + binary
        answer += binary
    print('#%d %s' %(tc, answer))