








# main
n = int(input())
paint = [input() for _ in range(n)]
for i in range(n):
    print(*paint[i])