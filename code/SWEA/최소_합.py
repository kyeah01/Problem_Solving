ways = [[0, 1], [1, 0]]
def guide(i, j, value):
    global N, matrix, minN
    if minN < value:
        return
    if [i, j] == [N-1, N-1]:
        minN = min(minN, value)
    for way in ways:
        x = i + way[0]
        y = j + way[1]
        if 0 <= x < N and 0 <= y < N:
            guide(x,y,value+matrix[x][y])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minN = 10*100
    guide(0,0,matrix[0][0])
    print(minN)
    # print(f'{tc}', minN)