from collections import deque

direction = ((0,1), (1,0), (0,-1), (-1,0))

def BFS():
    global N, M
    queue = deque([(0,0,1)])
    while queue:
        n = queue.popleft()
        for d in direction:
            nx, ny = n[0]+d[0], n[1]+d[1]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]:
                queue.append((nx, ny, n[2]+1))
                board[nx][ny] = 0
                if nx == N-1 and ny == M-1:
                    return n[2]+1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
print(BFS())