T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dummy = [int(input()) for _ in range(N)]
    ans = 0
    for d in dummy:
        ans += abs(d - sum(dummy)//N)
    print(f'#{tc}', ans//2)