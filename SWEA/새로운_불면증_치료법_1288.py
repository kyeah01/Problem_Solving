T  = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = set()
    times = 0
    while len(numbers) <= 9:
        times += 1
        numbers.update(str(n*times))
    print(f'#{tc}', times*n)