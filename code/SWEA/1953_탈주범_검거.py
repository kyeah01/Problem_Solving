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

def navi(N, M, R, C, L):
    queue = [[R, C]]
    visited = []
    while L:
        L -= 1
        length = len(queue)
        for _ in range(length):
            visited += [queue.pop(0)]
            i, j = visited[-1]
            ways = pipe[maps[i][j]]
            for way in ways:
                ni = i+way[0]
                nj = j+way[1]
                if 0<=ni<N and 0<=nj<M and maps[ni][nj] and [-way[0], -way[1]] in pipe[maps[ni][nj]]:
                    if [ni, nj] not in visited and [ni, nj] not in queue:
                        queue += [[ni, nj]]
    return len(visited)


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    print(navi(N, M, R,C,L))