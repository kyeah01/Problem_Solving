import itertools

arr = [1,2,3,4,5]

print([i for i in itertools.combinations_with_replacement(arr, 2)])