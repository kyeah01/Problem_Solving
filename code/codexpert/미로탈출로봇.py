def Quick_finder(start, end):
    direction = [0,0,1,-1]
    queue = [start]
    while queue:
        queue.pop(0)
        for d in range(4):
            

# main
# x가 가로, y가 세로.
x_size, y_size = map(int, input().split())
Sx, Sy, Ex, Ey = map(int, input().split())
maps = [list(map(int, input()) for _ in range(y_size)]

# 시작점을 큐에 저장하고
# 