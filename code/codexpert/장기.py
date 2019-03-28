def tracker(mal, zol):
    queue = [mal]
    time = -1
    visited = []
    while queue:
        time += 1
        for _ in range(len(queue)):
            mal = queue.pop(0)
            visited += [mal]
            for d in range(8):
                x = mal[0]+direction[d][0]
                y = mal[1]+direction[d][1]
                if 0<=x<M and 0<=y<N:
                    if mal == zol:
                        print(time)
                        return time
                    if (x,y) not in queue and (x,y) not in visited:
                        queue += [(x,y)]

direction = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]

N, M = map(int, input().split())
locate = list(map(int, input().split()))
mal = (locate[1]-1, locate[0]-1)
zol = (locate[3]-1, locate[2]-1)
tracker(mal, zol)