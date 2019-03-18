T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans, maxN = 0, 0
    for n in nums:
        if ans+n < 0:
            ans = 0
        else:
            ans += n
        maxN = max(ans, maxN)
    print(maxN)