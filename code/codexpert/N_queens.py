def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    direction = [(-1,-1),(1,1),(1,-1),(-1,1),(0,1),(1,0),(-1,0),(0,-1)]
    def can_i(i,j):
        for d in range(8):
            x = i+direction[d][0]
            y = j+direction[d][1]
            while 0<=x<n and 0<=y<n:
                if board[x][y]:
                    return False
                x += direction[d][0
                ]
                y += direction[d][1]
        return True
    
    def placement(i):
        nonlocal ans
        if i == n:
            ans += 1
            return
        for j in range(n):
            if can_i(i,j):
                board[i][j] = 'Q'
                placement(i+1)
                board[i][j] = 0
    ans = 0
    placement(0)
    print(ans)


n = int(input())
solution(n)
