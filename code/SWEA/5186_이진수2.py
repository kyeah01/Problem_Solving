T = int(input())
for tc in range(1, T+1):
    n = float(input())
    ans = ''
    while len(ans) < 13:
        n *= 2
        if n >= 1.0:
            if n == 1.0:
                ans += '1'
                break
            ans += '1'
            n -= 1
        else:
            ans += '0'
    else:
        ans = 'overflow'
    print(ans)