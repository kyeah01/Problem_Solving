def dice(n, m):
    arr = [0]*n
    def combination(k, m):
        if m < 0 or (n-k+1)*6 < m:
            return
        if k >= n:
            if not m:
                print(*arr[:])
            return
        for i in range(1,7):
            arr[k] = i
            combination(k+1, m-i)

    combination(0,m)

# main
N, M = map(int, input().split())
dice(N,M)