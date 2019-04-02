T = int(input())
for tc in range(1, T+1):
    y, m = map(int, input().split())
    m = m - (y-2016)
    if m < 0:
        y += m
        m = 13+m
        # 만약 m이 0이면 13월
    print(y, m)