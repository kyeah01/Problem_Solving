direction = [(0,1),(1,0),(0,-1),(-1,0)]
bound = set()

def blue_eraser(i,j):
    paint[i][j] = 0
    queue = [(i,j)]
    while queue:
        i,j = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if 0<=x<n and 0<=y<n and paint[x][y] == 'B' and (x,y) not in queue:
                queue += [(x,y)]
                paint[x][y] = 0

def red_eraser(i,j):
    global bound
    queue = [(i,j)]
    paint[i][j] = 0
    while queue:
        i,j = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if 0<=x<n and 0<=y<n and (x,y) not in queue:
                if paint[x][y] == 'R':
                    paint[x][y] = 0
                    queue += [(x,y)]
                elif paint[x][y] == 'G':
                    bound.update([(x,y)])

def green_eraser(i,j):
    flag = True
    queue = [(i,j)]
    paint[i][j] = 0
    if (i,j) in bound:
        flag = False
    while queue:
        i,j = queue.pop(0)
        for d in range(4):
            x = i+direction[d][0]
            y = j+direction[d][1]
            if 0<=x<n and 0<=y<n and (x,y) not in queue:
                if paint[x][y] == 'G':
                    queue += [(x,y)]
                    paint[x][y] = 0
                    if (x,y) in bound:
                        flag = False
    return flag

# main
n = int(input())
paint = [list(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'B':
            blue_eraser(i,j)
            cnt += 1
        elif paint[i][j] == 'R':
            red_eraser(i,j)
            cnt += 1
noncolor = cnt
for i in range(n):
    for j in range(n):
        if paint[i][j] == 'G':
            cnt += 1
            if green_eraser(i,j):
                noncolor += 1
print(cnt, noncolor)

