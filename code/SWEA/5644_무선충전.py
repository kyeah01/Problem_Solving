for tc in range(1, int(input())+1):
    maps = [[0 for _ in range(10)] for _ in range(10)]
    M, cnt = map(int, input().split())
    A, B = [0,0], [9,9]
    a_direction = input().split()
    b_direction = input().split()
    move = {0:(0,0), 1:(-1,0), 2:(0,1), 3:(1,0), 4:(0,-1)}
    AP = [list(map(int, input().split())) for _ in range(cnt)]

    for time in range(M):
        