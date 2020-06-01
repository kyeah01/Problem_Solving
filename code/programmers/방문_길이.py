def solution(dirs):
    directions = {'U': (-1, 0), 'D':(1, 0) , 'R':(0,1) , 'L':(0,-1)}
    x, y = 0,0
    already = []
    cnt = 0
    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if str(nx) + str(x) + str(ny) + str(y) not in already:
                already += [str(nx) + str(x) + str(ny) + str(y)]
                already += [str(x) + str(nx) + str(y) + str(ny)]
                cnt += 1
            x, y = nx, ny
    return cnt
