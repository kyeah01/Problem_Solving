def combination(arr, r):
    arr = sorted(arr)
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen += [arr[nxt]]
            generate(chosen)
            chosen.pop()
    generate([])


combination('ABCDE', 2)
combination([1, 2, 3, 4, 5], 3)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    check = [0 for _ in range(N)]
    