def solution(n):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    def blue_checker(i,j):
        queue = [(i,j)]
        while queue:
            i,j = queue.pop(0)
            for d in range(4):
                x = i+direction[d][0]
                y = j+direction[d][1]
                if 0<=x<n and 0<=y<n and (x,y) not in queue:
                    if paint[x][y] == 'B':
                        queue += [(x,y)]
                        paint[x][y] = 0
                        paint2[x][y] = 0
    
    def color(which,i,j):
        queue = [(i,j)]
        paint[i][j] = 0
        while queue:
            i,j = queue.pop(0)
            for d in range(4):
                x = i+direction[d][0]
                y = j+direction[d][1]
                if 0<=x<n and 0<=y<n and (x,y) not in queue:
                    if paint[x][y] == which:
                        queue += [(x,y)]
                        paint[x][y] = 0

    def noncolor(i,j):
        queue = [(i,j)]
        paint2[i][j] = 0
        while queue:
            i,j = queue.pop(0)
            for d in range(4):
                x = i+direction[d][0]
                y = j+direction[d][1]
                if 0<=x<n and 0<=y<n and (x,y) not in queue:
                    if paint2[x][y] in {'R', 'G'}:
                        queue += [(x,y)]
                        paint2[x][y] = 0
    cnt, ccnt = 0,0
    for i in range(n):
        for j in range(n):
            if paint2[i][j] == 'B':
                blue_checker(i,j)
                cnt += 1
                ccnt += 1
            else:
                if paint[i][j]:
                    cnt += 1
                    color(paint[i][j],i,j)
                if paint2[i][j]:
                    ccnt += 1
                    noncolor(i,j)
    print(cnt, ccnt)


# main
n = int(input())
paint = [list(input()) for _ in range(n)]
paint2 = [paint[i][:] for i in range(n)]
solution(n)
