def comb(k, mul):
    global n, result
    if n == k:
        if mul != 1:
            result += [mul]
        return
    comb(k+1, mul+numbers[k])
    comb(k+1, mul)

# main
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
comb(0, 0)
print(sorted(list(set(result)))[::-1].index(k)+1)