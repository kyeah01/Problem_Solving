def finder(n, m, trees):
    def sumit(val):
        result = 0
        for i in range(n-1, 0, -1):
            if trees[i] <= val:
                break
            result += trees[i]-val
        return result

    def binary(m):
        s, e = 0, max(trees)
        while s < e:
            mid = (s+e)//2
            result = sumit(mid)
            if result == m:
                return mid
            if result < m:
                e = mid+1
            else:
                sol = mid
                s = mid
        return sol
    return binary(m)

# main
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
print(finder(n,m,trees))