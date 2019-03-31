def comb(k, cnt, total):
    global n,ans, maxN
    if cnt == n//2:
        ans = min(ans, abs(total-(maxN-total)))
        return
    if n == k:
        return
    comb(k+1, cnt+1, total+tape[k])
    comb(k+1, cnt, total)
    # 20에서 10개를 구하는 경우를 구하면 되겠군!!

# main
n = int(input())
tape = list(map(int, input().split()))
ans = 500*20
maxN = sum(tape)
comb(0, 0, 0)
print(ans)