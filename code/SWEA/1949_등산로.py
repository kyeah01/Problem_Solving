def finder(i,j):
    stack = [(i,j)]
    visited[i][j] = 1
    cnt = 1
    maxN = 0
    d = 0
    value = maps[i][j]
            # 스택으로 돌릴때는 길을 찾을때마다 가는 게 아니라 길을 찾으면 바로 거기로 직진하고,
            # 그 다음에 계속 가다가, 만약에 갈 수 있는 길이 없으면 스택에서 pop을 해서 다음을 찾아야 함.
            # 결론적으로, 스택에서 pop을 하는 시기는 bfs처럼 4번의 길찾기가 끝낫을때가 아니라 
            # 4방향 어디를 찾아도 길을 찾지 못할때다.
    print(maxN)
    
            
                
# T = int(input())
T = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 인풋
for tc in range(1,T+1):
    N, K = map(int, input().split())
    # maps = [list(map(int, input().split())) for _ in range(N)]
    maps = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]
    
    # max값인지 확인하고, 그 뒤에 탐색을 시작하자.
    maxN = 0
    for i in range(N):
        maxN = max(maxN, max(maps[i]))
    for i in range(N):
        for j in range(N):
            if maps[i][j] == maxN:
                visited = [[0 for _ in range(N)] for _ in range(N)]
                visited[i][j] = 1
                finder(i,j)