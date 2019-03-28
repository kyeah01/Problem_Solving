def BFS(sang, wang):
    queue = [sang]
    time = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            i,j = queue.pop(0)
            for k,v in directions.items():
                if 0 <= i+k[0] < 10 and 0 <= j+k[1] < 9 and (i+k[0], j+k[1]) not in queue:
                    if (i+k[0], j+k[1]) == wang:
                        return time
                    check = []
                    for d in range(2):
                        if not d:
                            check += [(i+v[d][0], j+v[d][1])]
                        else:
                            check += [(check[-1][0]+v[d][0], check[-1][1]+v[d][1])]
                    if wang not in check:
                        queue += [(i+k[0], j+k[1])]
    return time


directions = { (-3,-2) : ((-1,0),(-1,-1),(-1,-1)),
               (-2,-3) : ((0,-1),(-1,-1),(-1,-1)),
               (2,-3) : ((0,-1),(1,-1),(1,-1)),
               (3,-2) : ((1,0),(1,-1),(1,-1)),
               (3,2) : ((1,0),(1,1),(1,1)),
               (2,3) : ((0,1),(1,1),(1,1)),
               (-2,3) : ((0,1),(-1,1),(-1,1)),
               (-3,2) : ((-1,0),(-1,1),(-1,1))}

sang = tuple(map(int, input().split()))
wang = tuple(map(int, input().split()))
print(BFS(sang, wang))
