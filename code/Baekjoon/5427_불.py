direction = ((0,1), (1,0), (-1,0), (0,-1))
def check():
    global h, w
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                return True
    return False

def fire():
    global h, w
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '*':
                for d in direction:
                    nx, ny = i+d[0], j+d[1]
                    if 0<=nx<h and 0<=ny<w:
                        maps[nx][ny] = '*'

def move():
    global h, w
    queue = [(i, j, 0) for i in range(h) for j in range(w) if maps[i][j] == '@']
    ep = 0
    while queue:
        n = queue.pop(0)
        for d in direction:
            nx, ny = n[0]+d[0], n[1]+d[1]
            print(nx, ny)
            if 0<=nx<w and 0<=ny<h:
                if maps[nx][ny] == '.':
                    maps[nx][ny] = '@'
                    queue += [(nx, ny, n[2]+1)]
            else:
                return n[2]
        if ep < n[2]:
            fire()
            if not check():
                return 'IMPOSSIBLE'
            ep += 1
            


for tc in range(int(input())):
    w, h = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    print(move())