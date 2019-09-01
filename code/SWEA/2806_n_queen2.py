def diagonal(arr, k):
    for x in range(k):
        if abs(x - k) == abs(arr[x] - arr[k]):
            return False
    return True

def comb(arr,k,n):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(N):
        if i not in arr[:k]:
            arr[k] = i
            if diagonal(arr, k):
                comb(arr, k+1, n)


for tc in range(1, int(input())+1):
    cnt = 0
    N = int(input())
    arr = [-1 for _ in range(N)]
    comb(arr,0,N)
    print(cnt)