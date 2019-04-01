direction = {'0':(),
             '1':((0,-1),(0,1)),
             '2':((-1,0),(1,0)),
             '3':((1,0),(0,1)),
             '4':((0,-1),(1,0)),
             '5':((0,-1),(-1,0)),
             '6':((-1,0),(0,1)),
             '7':((-1,0),(0,1),(1,0)),
             '8':((0,-1),(0,1),(1,0)),
             '9':((-1,0),(0,-1),(1,0)),
             'A':((0,-1),(-1,0),(0,1)),
             'B':((0,-1),(0,1),(1,0),(-1,0))}


def BFS_finder(i,j):
    queue = [(i,j)]
    cnt = 1
    while queue:
        i,j = queue.pop(0)
        nxt = direction[board[i][j]]
        board[i][j] = '0'
        for d in range(len(nxt)):
            x = i+nxt[d][0]
            y = j+nxt[d][1]
            if 0<=x<n and 0<=y<n and board[x][y] != '0' and (-nxt[d][0], -nxt[d][1]) in direction[board[x][y]] and (x,y) not in queue:
                queue += [(x,y)]
                cnt += 1
    return cnt


# main
n = int(input())
y, x = map(int,input().split())
board = [list(input()) for _ in range(n)]
print(sum(1 for i in range(n) for j in range(n) if board[i][j] != '0') - BFS_finder(x,y))
