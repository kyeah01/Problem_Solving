import itertools

arr = [1,2,3,4,5]

print([i for i in itertools.combinations(arr, 1)])

for i in range(len(arr)+1):
    print([j for j in itertools.combinations(arr, i)])