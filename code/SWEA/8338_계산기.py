import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = numbers[0]
    if N == 1:
        print('#{}'.format(tc), numbers[0])
    else:
        for num in numbers[1:]:
            ans = max((ans+num),(ans*num))
    print('#{}'.format(tc), ans)