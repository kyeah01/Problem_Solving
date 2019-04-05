def solution():
    def comb(n):
        nonlocal result
        # 조합을 만들어야 하는데, K개 이상 선택하게 조합을 만들어야 함.
        # powerset으로 sum이 K가 되게 하면 되겠다.
        if n == D:
            if D-pwst.count(0) > result:
                return
            temp = [film[i][:] for i in range(D)]
            for i in range(D):
                # print(D-pwst.count(0))
                if pwst[i] == 1:
                    temp[i] = [1 for _ in range(W)]
                elif pwst[i] == 2:
                    temp[i] = [0 for _ in range(W)]
            if chk(temp):
                result = min(result, D-pwst.count(0))
            return
        comb(n+1)
        pwst[n] = 1
        comb(n+1)
        pwst[n] = 2
        comb(n+1)
        pwst[n] = 0

    def chk(arr):
        for j in range(W):
            save = arr[0][j]
            cnt = 1
            for i in range(D):
                if cnt >= K:
                    break
                if arr[i][j] == save:
                    cnt += 1
                else:
                    save = arr[i][j]
                    cnt = 1
            else:
                return False
        return True

    result = 0xffffff
    pwst = [0]*D
    if chk(film):
        print('#{}'.format(tc), 0)
    else:
        comb(0)
        print('#{}'.format(tc), result)


T = int(input())

for tc in range(1, T+1):
    # D는 세로, W는 가로, K는 합격기준
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    solution()