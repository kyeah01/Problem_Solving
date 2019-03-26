import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    queue = [list(map(int, input().split())) for _ in range(N)]
    queue.sort()
    order = [queue.pop(0)]
    while queue:
        nxt = queue.pop(0)
        if nxt[0] >= order[-1][1]:
            order += [nxt]
        else:
            versus = order.pop()
            order += [min([versus, nxt], key=lambda x:x[1])]
    print('#{}'.format(tc), len(order))