import sys
sys.stdin = open('input.txt', 'r')


direction = ((0,1), (1,0), (0,-1), (-1,0))

# board[i][j]가 2이상이면 여기에 옵니다!
def pang(i,j):
    check = [[[0,0,0,0] for _ in range(W)] for _ in range(H)]
    check[i][j] = [board[i][j]]*4
    count = board[i][j]
    # 그래서 count는 항상 2이상
    for d in range(4):
        for k in range(board[i][j]):
            




for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    marbles = [0]*4
    for i in range(4):
        for j in range(W):
            # j번에 위치한 구슬을 깬다.
            # 만약 아무것도 없으면? 다음으로 넘어간다.
            for h in range(H):
                if board[h][j]:
                    # 구슬 팡!!!!
                    board[h][j]
                    # 그리고 밑으로 떨굼
                    break

    # 모든 과정이 끝남