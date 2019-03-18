T = int(input())

for tc in range(1, T+1):
    ans = 0
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    height, start, length = 0, N//2, 1
    while height < N:
        ans += sum(farm[height][start:start+length])
        height += 1
        if height > N//2:
            length -= 2
            start += 1
        else:
            length += 2
            start -= 1
    print(f'#{tc}', ans)