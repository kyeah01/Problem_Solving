T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}')
    answer = ''
    for _ in range(n):
        letter, times = input().split()
        answer += letter*int(times)
    for i in range(len(answer)):
        if i%10 == 9:
            print(answer[i])
        else:
            print(answer[i], end='')