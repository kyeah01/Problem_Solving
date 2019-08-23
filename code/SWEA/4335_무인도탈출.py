import sys
from itertools import permutations


sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    boxs = [list(map(int, input().split())) for _ in range(N)]

    permu = []
    for i in range(len(boxs), 0, -1):
        height = 0
        for tower in permutations(boxs, i):
            tmp = tower[0]
            h = 0
            for box in tower:
                if tmp[0] < box[0] or tmp[1] < box[1]:
                    break
                else:
                    h += box[2]
            height = max(height, h)
        if height:
            print(height)
            break
