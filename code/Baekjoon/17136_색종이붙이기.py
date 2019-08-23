def check(x, y, k):
    # x, y 좌표에서 k 크기의 색종이를 붙일 수 있는지 판별함
    if x+k >= 10 and y+k >= 10:
        return False
    for i in range(x, x+k+1):
        for j in range(y, y+k+1):
            if not board[i][j]:
                return False
    # 붙일 수 있는 거 확인했으니, x, y 좌표에서 k 크기의 색종이를 붙임
    for i in range(x, x+k+1):
        for j in range(y, y+k+1):
                board[i][j] = 0

def DFS():
    for k in range(5):
        for i in range(10):
            for j in range(10):
                if paper[k-1]:
                    if check(i,j,k):
                        paper[k-1] -= 1
    for i in range(10):
        for j in range(10):
            if board[i][j]:
                return -1
    return 25-sum(paper)


board = [list(map(int, input().split())) for _ in range(10)]
paper = [5,5,5,5,5]
print(DFS())