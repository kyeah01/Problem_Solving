directions = {
    1:(-1,0),
    2:(1,0),
    3:(0,1),
    4:(0,-1)
}
def pprint():
    for i in range(R):
        print(*sea[i])

def fishing(i):
    for j in range(C):
        if sea[i][j]:
            weight = sea[i][j][2]
            sea[i][j] = (0,0,0)
            return weight

def jaws():
    for i in range(R):
        for j in range(C):
            if sea[i][j][2]:
                # 거기 상어가 있어!!
                


def solution():


R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
sea = [[(0,0,0) for _ in range(C)] for _ in range(R)]
for r,c,s,d,z in sharks:
    sea[r-1][c-1] = (s, d, z)