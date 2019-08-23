from collections import deque

tunnel = {
    1: ((0,-1),(0,1),(1,0), (-1,0)),
    2: ((-1,0),(1,0)),
    3: ((0,-1),(0,1)),
    4: ((-1,0),(0,1)),
    5: ((0,1), (1,0)),
    6: ((0,-1), (1,0)),
    7: ((0,-1), (-1,0))
}


def BFS(r, c, l):
    global N, M
    queue = deque([(r,c,maps[r][c], 1)])
    maps[r][c] = 0
    cnt = 1
    while queue:
        n = queue.popleft()
        if n[3] < l:
            for d in tunnel[n[2]]:
                nx, ny = n[0]+d[0], n[1]+d[1]
                if 0<=nx<N and 0<=ny<M and maps[nx][ny] and (-d[0], -d[1]) in tunnel[maps[nx][ny]]:
                    queue.append((nx, ny, maps[nx][ny], n[3]+1))
                    maps[nx][ny] = 0
                    cnt += 1
    return cnt



for tc in range(1, int(input())+1):
    # 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 
    N, M, R, C, L = map(int, input().split())
    # 그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', BFS(R, C, L))