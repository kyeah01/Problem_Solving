def finder(n, m, trees):
    def sumit(val):
        # result = 0
        # for i in range(n-1, 0, -1):
        #     if trees[i] <= val:
        #         break
        #     result += trees[i]-val
        result = sum(trees[i]-val for i in range(n) if trees[i]>val)
        return result

    def binary(m):
        s, e = 0, max(trees)+1
        while s < e:
            mid = (s+e)//2
            result = sumit(mid)
            if s+1 == e:
                return e
            if result == m:
                return mid
            if result < m:
                e = mid
            else:
                s = mid
        return sol
    return binary(m)

# 1과 2사이의 값을 찾아야 할때
# 그럼 값을 1.**로 나오게 만들어보자
# 


# main
n, m = map(int, input().split())
trees = list(map(int, input().split()))
# trees.sort()
print(finder(n,m,trees))