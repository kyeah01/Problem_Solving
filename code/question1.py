def BFS(N, cards):
    queue = [(0, cards, 0)]
    while queue:
        n = queue.pop(0)
        if n[1] in (sorted(cards), sorted(cards, reverse)):
            return n[2]
        for i in range(1, N):
            

    return -1


if __name__ == '__main__':
    for tc in range(1, int(input())):
        N = int(input())
        cards = list(map(int, input().split()))