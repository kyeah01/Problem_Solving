def Quick_finder(start, end):
    direction = [0,0,1,-1]
    queue = [start]
    while queue:
        i,j,t = queue.pop(0)
        for d in range(4):
            x = i+direction[d]
            y = j+direction[::-1][d]
            if 0<=x<x_size and 0<=y<y_size and not maps[x][y]:
                if (x,y) == end:
                    print(t+1)
                    return t+1
                if (x,y) not in queue:
                    queue += [(x,y, t+1)]
                    maps[x][y] = 1

# main
# x가 가로, y가 세로.
y_size, x_size = map(int, input().split())
Sy, Sx, Ey, Ex = map(int, input().split())
maps = [list(map(int, input())) for _ in range(x_size)]
start = (Sx-1, Sy-1, 0)
end = (Ex-1, Ey-1)
Quick_finder(start,end)