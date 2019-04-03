def solution():
    # global minN
    queue = [(0,0)]
    while queue:
        i,j = queue.pop(0)
        for d in range(4):
            x = i+direct[d][0]
            y = j+direct[d][0]
            if 0<=x<n and 0<=y<n and not in queue:
        



direct = [(0,1), (0,-1), (1,0), (-1,0)]

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
minN = 