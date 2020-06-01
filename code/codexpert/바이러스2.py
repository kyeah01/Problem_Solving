def solution():
    stack = [1]
    visited = [1]
    while stack:
        n = stack.pop()
        for i in range(m):
            if n == networks[i][0] and networks[i][1] not in visited:
                visited += [networks[i][1]]
                stack += [networks[i][1]]
            elif n == networks[i][1] and networks[i][0] not in visited:
                visited += [networks[i][0]]
                stack += [networks[i][0]]
    return visited


n = int(input())
m = int(input())
networks = [list(map(int, input().split())) for _ in range(m)]
print(solution())