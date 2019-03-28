def sumit(n, total):
    if not n:
        return total
    return sumit(n-1, total+n)

# main
n = int(input())
print(sumit(n, 0))