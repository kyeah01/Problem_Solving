def solution():
    # 밑으로 떨어지게 하자.
    def gravity():
        for j in range(n):
            for i in range(n):
                if bricks[i][j]:
                    k = i
                    while k<n and bricks[k][j]:
                        k += 1
                    if k != n:
                        