N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]

for first in price[0]:
    # 오직 첫번째 집만 세번 모두 수행한다.
    # 결론적으로는 세개의 밸류가 생김.