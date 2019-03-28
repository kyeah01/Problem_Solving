def apt(n, maps):
    def changer(n):
        for i in range(n):
            for j in range(n):
                if maps[i][j]:
                    maps[i][j] = 'a'

    # DFS로 검색
    def numbering(num,i,j):
        nonlocal total
        for d in range(4):
            x = i+dx[d]
            y = j+dy[d]
            if 0<=x<n and 0<=y<n:
                if maps[x][y] == 'a':
                    maps[x][y] = num
                    total += 1
                    numbering(num,x,y)
    
    def numbering_BFS(num, i, j):
        queue = [[i,j]]
        total = 0
        while queue:
            i,j = queue.pop(0)
            for d in range(4):
                x = i+dx[d]
                y = j+dy[d]
                if 0<=x<n and 0<=y<n:
                    if maps[x][y] == 'a':
                        maps[x][y] = num
                        total += 1
                        queue += [[x,y]]
        return total
            

    def finder(n):
        nonlocal total
        num = 0
        result = []
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 'a':
                    num += 1
                    total = 0
                    # # DFS
                    # numbering(num, i, j)
                    # result += [total if total else 1]
                    # BFS
                    nxt = numbering_BFS(num, i, j)
                    result += [nxt if nxt else 1]
        return [num]+result
    
    changer(n)
    total = 0
    return finder(n)


# main
dx = (0,0,1,-1)
dy = (1,-1,0,0)

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
result = apt(n, maps)
result = [result[0]] + sorted(result[1:])

for i in result:
    print(i)