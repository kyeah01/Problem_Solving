T = int(input())

for tc in range(1, T+1):
    N = int(input())
    days = list(map(int, input().split()))
    max_index = N-(days[::-1].index(max(days))+1)
    ans = 0
    # max_index까지 값을 구해야함
    for i in range(max_index):
        ans += max(days) - days[i]
    if ans < 0:
        ans = 0