def solution(start, end):
    queue = [(start[0]-1, start[1]-1, start[2], 0)]
    while queue:
        # print(queue)
        i,j,d,c = queue.pop(0)
        if (i,j,d) == (end[0]-1, end[1]-1, end[2]):
            print(c)
            return
        # 0칸, 1칸 2칸 3칸가는 경우
        for k in range(1,4):
            x = i+direction[d][0]*k
            y = j+direction[d][1]*k
            if 0<=x<m and 0<=y<n and not maps[x][y]:
                if not visited[d][x][y]:
                    queue += [(x,y,d,c+1)]
                    visited[d][x][y] = 1
            else: break
        for l in range(2):
            # 내가 그 방향을 가본 적이 있냐 없냐에 대한 체크를 하면 됨.
            nd = turn[d][l]
            if not visited[nd][i][j]:
                queue += [(i,j,nd,c+1)]
                visited[nd][i][j] = 1


direction = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
turn = ((0,0),(3,4),(4,3),(2,1),(1,2))
m,n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
visited = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(5)]
solution(start, end)