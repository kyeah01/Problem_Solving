def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    bridge = {i:{j:0 for j in range(n)} for i in range(n)}
    visitedIsland = [costs[0][0]]
    totalCost = 0
    while len(visitedIsland) < n:
        for cost in costs:
            if not bridge[cost[0]][cost[1]] and (cost[0] not in visitedIsland or cost[1] not in visitedIsland):
                if cost[0] not in visitedIsland and cost[1] not in visitedIsland:
                    continue
                bridge[cost[0]][cost[1]] = 1
                bridge[cost[1]][cost[0]] = 1
                visitedIsland += [c for c in [cost[0], cost[1]] if c not in visitedIsland]
                totalCost += cost[2]
                break
    return totalCost
