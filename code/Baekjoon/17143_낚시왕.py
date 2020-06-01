directions = {
    1:(-1,0),
    2:(1,0),
    3:(0,1),
    4:(0,-1)
}
change = {
    1:2,
    2:1,
    3:4,
    4:3
}

def fishing(j):
    global M
    match = []
    for i in range(M):
        if shark_locations[i][1] == j:
            match += [i]
    if match:
        w = shark_locations[sorted(match)[0]][4]
        shark_locations[sorted(match)[0]] = (0,0,0,0,0)
        return w
    else:
        return 0

def move(speed, d, now):
    if directions[d][0]:
        speed %= ((R-1)*2)
    if directions[d][1]:
        speed %= ((C-1)*2)

    for _ in range(speed):
        nx, ny = now[0]+directions[d][0], now[1]+directions[d][1]
        if not 0 <= nx < R or not 0 <= ny < C:
            d = change[d]
        now = (now[0]+directions[d][0], now[1]+directions[d][1])
    return (now[0], now[1], d)

def jaws():
    visited = {}
    for i in range(M):
        if shark_locations[i][4]:
            now = shark_locations[i]
            nx, ny, d = move(now[2], now[3], (now[0], now[1]))
            if (nx, ny) in visited.keys():
                if now[4] > shark_locations[visited[(nx, ny)]][4]:
                    shark_locations[visited[(nx, ny)]] = (0, 0, 0, 0, 0)
                    shark_locations[i] = (nx, ny, now[2], d, now[4])
                    visited[(nx, ny)] = i
                else:
                    shark_locations[i] = (0,0,0,0,0)

            else:
                shark_locations[i] = (nx, ny, now[2], d, now[4])
                visited[(nx, ny)] = i


def solution():
    total = 0
    for c in range(C):
        total += fishing(c)
        jaws()
    return total

R, C, M = map(int, input().split())
shark_locations = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    n = shark_locations[i]
    shark_locations[i] = [n[0]-1, n[1]-1, n[2], n[3], n[4]]
print(solution())
for i in range(M):
    print(*shark_locations[i])