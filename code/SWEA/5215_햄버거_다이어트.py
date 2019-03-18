def tasty_road():
    # 전형적인 냅색문제



T = int(input())
for tc in range(1, T+1):
    ingredients, max_calorie = map(int, input().split())
    tasty = [list(map(int, input().split())) for _ in range(N)]
    cost, value = 0, []
    for i in range(N):
        if cost + tasty