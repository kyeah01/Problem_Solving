def solution(n):
    result = [[[], []] for _ in range(n)]
    temp = list(range(1, n+1))[::-1]
    i = 0
    position = [-1, 0]
    directions = [(1, 0), (0, 0), (-1, 1)]
    now = 0
    k = 1
    while k <= n*(n+1)//2:
        while i < len(temp) and temp[i]:
            position = [position[0] + directions[now][0], directions[now][1]]
            if position[1]:
                result[position[0]][position[1]].insert(0, k)
            else:
                result[position[0]][position[1]] += [k]
            k += 1
            temp[i] -= 1
        i += 1
        now = now + 1 if now < 2 else 0
    return [d3 for d1 in result for d2 in d1 for d3 in d2]

print(solution(4))