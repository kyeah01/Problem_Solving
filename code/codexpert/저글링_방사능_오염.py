def nuclear(target):
    global height, width, dx, dy
    queue = [[target[0]-1, target[1]-1]]
    time = 0
    while queue:
        # print(queue)
        # for i in range(height):
        #     print(*maps[i])
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            maps[x][y] = 0
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0<=nx<height and 0<=ny<width:
                    if maps[nx][ny]:
                        if (nx, ny) not in queue:
                            queue += [(nx, ny)]
        time += 1
    result = 0
    for j in range(height):
        result += sum(maps[j])
    return time+2, result

dx = (0,0,1,-1)
dy = (1,-1,-0,0)
# main
width, height = map(int, input().split())
maps = [list(map(int, input())) for _ in range(height)]
target = tuple(map(int, input().split()))[::-1]
for i in nuclear(target):
    print(i)


