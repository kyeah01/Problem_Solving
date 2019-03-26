def casher(n, cost):
    arr = list(range(n))
    result = []
    min_cost = 100*60
    def permutation(n, k, total_cost):
        nonlocal arr, result, min_cost
        if min_cost < total_cost:
            return
        if n == k:
            # print(arr[:])
            min_cost = min(min_cost, total_cost+cost[arr[-1]][0])
        else:
            for i in range(k, n):
                arr[k], arr[i] = arr[i], arr[k]
                # print(k-1, k, arr[k-1], arr[k], cost[arr[k-1]][arr[k]])
                if k > 0:
                    permutation(n, k+1, total_cost+cost[arr[k-1]][arr[k]])
                else:
                    permutation(n, k+1, total_cost)
                arr[k], arr[i] = arr[i], arr[k]
    permutation(n, 1, 0)
    return min_cost

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(tc),casher(N, cost))