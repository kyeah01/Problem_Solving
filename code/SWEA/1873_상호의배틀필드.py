# 하라는대로 하는 시뮬레이션 문제.
direction = {
    'U' : (-1,0,'^'),
    'D' : (1,0,'v'),
    'L' : (0,-1,'<'),
    'R' : (0,1,'>'),
    '^' : 'U',
    'v' : 'D',
    '<' : 'L',
    '>' : 'R'
}
def solution(H, W):
    x, y = finder(H,W)
    for a in act:
        if a == 'S':
            shooting(x,y,direction[direction[maps[x][y]]])
        else:
            maps[x][y] = direction[a][2]
            nx, ny = x+direction[a][0], y+direction[a][1]
            if 0<=nx<H and 0<=ny<W and maps[nx][ny] =='.':
                maps[nx][ny], maps[x][y] = maps[x][y], maps[nx][ny]
                x, y = nx, ny

def finder(H, W):
    for i in range(H):
        for j in range(W):
            if maps[i][j] in ('<', '>', '^', 'v'):
                # 거기가 전차가 최초로 놓인 위치
                return (i,j)

def shooting(x,y,d):
    while True:
        x += d[0]
        y += d[1]
        if 0>x or x>=H or 0>y or y>=W:
            return
        elif maps[x][y] == '#':
            return 
        elif maps[x][y] == '*':
            maps[x][y] = '.'
            return


def pprint(tc, H,W):
    print('#{}'.format(tc), end=' ')
    for i in range(H):
        print(*maps[i])

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    N = int(input())
    act = list(input())
    solution(H, W)
    pprint(tc, H,W)