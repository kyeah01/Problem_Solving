arrow = {
    'u' : (-1,0),
    'd' : (1,0),
    'l' : (0,-1),
    'r' : (0,1)
}
directions = {
    1 : (
            ( arrow['r'],), 
            ( arrow['d'],),
            ( arrow['u'],),
            ( arrow['l'],)
        ),
    2 : (
            ( arrow['l'], arrow['r'] ),
            ( arrow['u'], arrow['d'] )
    ),
    3 : (
            ( arrow['u'], arrow['r'] ),
            ( arrow['r'], arrow['d'] ),
            ( arrow['d'], arrow['l'] ),
            ( arrow['l'], arrow['u'] )
        ),
    4 : (
            ( arrow['l'], arrow['u'], arrow['r'] ),
            ( arrow['u'], arrow['r'], arrow['d'] ),
            ( arrow['r'], arrow['d'], arrow['l'] ),
            ( arrow['d'], arrow['l'], arrow['u'] )
        ),
    5 : (
            (arrow['r'], arrow['d'], arrow['l'], arrow['u']),
        )
}



def solution(N, M, maps):
    def comb(k, n):
        if k == n:
            # 일해라
            visitor()
            return
        for i in directions[locations[k][2]]:
            arr[k] = i
            comb(k+1, n)
    
    def visitor():
        nonlocal cnt
        visited = []
        for i in range(len(arr)):
            for d in arr[i]:
                if d == (1,0):
                    for x in range(locations[i][0]+1, N):
                        # print(x, locations[i][1], d, locations[i])
                        if maps[x][locations[i][1]] == 6:
                            break
                        if not maps[x][locations[i][1]]:
                            visited += [(x, locations[i][1])]
                if d == (-1,0):
                    for x in range(locations[i][0]-1, -1, -1):
                        # print(x, locations[i][1], d, locations[i])
                        if maps[x][locations[i][1]] == 6:
                            break
                        if not maps[x][locations[i][1]]:
                            visited += [(x, locations[i][1])]
                if d == (0,1):
                    for y in range(locations[i][1]+1, M):
                        # print(locations[i][0], y, d, locations[i])
                        if maps[locations[i][0]][y] == 6:
                            break
                        if not maps[locations[i][0]][y]:
                            visited += [(locations[i][0], y)]
                if d == (0,-1):
                    for y in range(locations[i][1]-1, -1, -1):
                        # print(locations[i][0], y, d, locations[i])
                        if maps[locations[i][0]][y] == 6:
                            break
                        if not maps[locations[i][0]][y]:
                            visited += [(locations[i][0], y)]
        cnt = max(cnt, len(set(visited)))


    locations = [(i,j,maps[i][j]) for i in range(N) for j in range(M) if maps[i][j] in (1,2,3,4,5)]
    arr = [0 for _ in range(len(locations))]
    cnt = 0
    comb(0, len(arr))
    # print(cnt)
    print(N*M - sum(1 for i in range(N) for j in range(M) if maps[i][j]) - cnt)

if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    solution(N, M, maps)