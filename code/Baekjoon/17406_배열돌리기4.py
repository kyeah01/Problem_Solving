def turning(arr):
    for (r,s,c) in arr:
        start, end = (r-s, c-s), (r+s, c+s)
        


def perm(k, n, arr, visited):
    if k == n:
        print(arr)
        return
    for i in range(n):
        if i not in visited:
            arr[k] = i
            perm(k+1, n, arr, visited+[i])


# perm(0, 3, [0,0,0], [])

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
turn = [list(map(int, input().split())) for _ in range(K)]
perm(0, len(turn), [0 for _ in range(len(turn))], [])
