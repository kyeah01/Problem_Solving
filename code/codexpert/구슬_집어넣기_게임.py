def solution(red, blue, goal):
    queue = [(red[0], red[1], blue[0], blue[1], 0)]
    while queue:
        rx, ry, bx, by, cnt = queue.pop(0)
        for d in range(4):
            nrx, nry = rx+direction[d][0], ry+direction[d][1]
            nbx, nby = bx+direction[d][0], by+direction[d][1]
            if (nrx, nry) != (nbx, nby) and (nrx, nry) == goal:
                print(cnt)
                return cnt
            if cnt == 10:
                print(-1)
                return
            if board[nrx][nry] == '#':
                nrx, nry = rx, ry
            if board[nbx][nby] == '#':
                nbx, nby = bx, by
            if (nrx, nry) == (nbx, nby): continue
                # visited에 있으면서,
                #         1. 값이 있는 경우는 다음으로 넘어가야 함.
                #         2. 값이 없는 경우는 업데이트 시켜 줘야 함.
                # visited에 없으면, 업데이트시켜줘서 비지트 처리 해야 함.
            if visited.get((nrx, nry)):
                if (nbx, nby) in visited[(nrx, nry)]: continue
                else:
                    queue += [(nrx, nry, nbx, nby, cnt+1)]
                    visited[(nrx, nry)] += [(nbx, nby)]
            else:
                queue += [(nrx, nry, nbx, nby, cnt+1)]
                visited[(nrx, nry)] = [(nbx, nby)]



direction = ((0,1),(1,0),(0,-1),(-1,0))
T = int(input())
for tc in range(1, T+1):
    x_size, y_size = map(int, input().split())
    board = [list(input()) for _ in range(x_size)]
    for i in range(x_size):
        for j in range(y_size):
            if board[i][j] == 'B':
                blue = (i,j)
            elif board[i][j] == 'R':
                red = (i,j)
            elif board[i][j] == 'H':
                goal = (i,j)
    visited = {}
    solution(red, blue, goal)
    # print(visited)