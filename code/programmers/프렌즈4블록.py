def solution(m, n, board):
    board = [list(b) for b in board]
    deleteBlock = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0
    sumValue = 1
    while sumValue:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != 0:
                    deleteBlock[i][j] = 1
                    deleteBlock[i+1][j] = 1
                    deleteBlock[i][j+1] = 1
                    deleteBlock[i+1][j+1] = 1
        sumValue = sum(1 for i in range(m) for j in range(n) if deleteBlock[i][j] == 1)
        cnt += sumValue
        
        if sumValue:
            for j in range(n):
                moveBlocks = [board[i][j] for i in range(m) if deleteBlock[i][j] == 0]
                moveBlocks = [0 for _ in range(m-len(moveBlocks))] + moveBlocks
                for i in range(m):
                    board[i][j] = moveBlocks[i]
        deleteBlock = [[0 for _ in range(n)] for _ in range(m)]
    return cnt
