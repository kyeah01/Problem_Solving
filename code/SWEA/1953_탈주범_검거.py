import sys
sys.stdin = open('input.txt')



pipe = {
    1 : [[-1,0],[0,1],[1,0],[0,-1]],
    2 : [[-1,0],[1,0]],
    3 : [[0, -1], [0, 1]],
    4 : [[-1, 0],[0,1]],
    5 : [[1, 0],[0, 1]],
    6 : [[0, -1],[1, 0]],
    7 : [[0, -1],[-1, 0]]
}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    navi(R,C,L)
    print(cnt)
    for i in range(N):
        print(*maps[i])