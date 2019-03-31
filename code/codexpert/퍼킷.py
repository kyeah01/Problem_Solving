def comb(k, sour, bitter):
    global n, ans
    if n == k:
        if sour != 1 and bitter != 1:
            ans = min(ans, abs(sour-bitter))
        return
    comb(k+1, sour*ingredient[k][0], bitter+ingredient[k][1])
    comb(k+1, sour, bitter)

n = int(input())
ingredient = [list(map(int, input().split())) for _ in range(n)]
ans = 10000000000
comb(0,1,0)
print(ans)