def porter(containers, trucks):
    cnt = 0
    while containers and trucks:
        nxt_container = containers.pop()
        nxt_truck = trucks.pop()
        if nxt_truck >= nxt_container:
            cnt += nxt_container
        else:
            trucks += [nxt_truck]
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()
    print('#{}'.format(tc), porter(containers, trucks))