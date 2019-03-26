N = int(input())
candys = list(map(int, input().split()))

total = 0
while len(candys) > 1:
    price = candys.pop(candys.index(min(candys))) + candys.pop(candys.index(min(candys)))
    total += price
    candys += [price]

print(total)