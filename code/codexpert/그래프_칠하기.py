def solution():
    for i in range(n):
        palette = list(range(1,m+1))
        for j in range(len(edges[i])):
            if edges[i][j]:
                if color[j] in palette:
                    palette.remove(color[j])
            if palette:
                color[i] = palette[0]
            else:
                return [-1]
    return color


n,m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n)]
color = [0]*n

print(*solution())