from itertools import permutations

def prmt(arr):
    already = []
    for k in range(1, len(arr)+1):
        for num in permutations(arr, k):
            temp = int(''.join(num))
            if temp not in already:
                already += [temp]
                yield temp

def primeChecker(number):
    if number in (0, 1):
        return False
    if number in (2, 3, 5, 7):
        return True
    for i in range(2, number//2 + 2):
        if number % i == 0:
            return False
    return True

def primeMaker(numbers):
    count = 0
    for num in prmt(numbers):
        if primeChecker(num):
            count += 1
    return count
                
def solution(numbers):
    numbers = list(numbers)
    return primeMaker(numbers)
