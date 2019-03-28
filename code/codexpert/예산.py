# 바이너리 서치
def finder(arr):
    global n, max_budget

    def total_cost(avg):
        total = 0
        for i in range(n):
            total += min(avg, arr[i])
        return total
    
    def binarysearch(max_budget):
        s, e = 0, max(arr)
        sol = 0
        while s <= e:
            mid = (s+e)//2
            total = total_cost(mid)
            if total == max_budget:
                return mid
            elif total > max_budget:
                e = mid-1
            else:
                sol = mid
                s = mid+1
        return sol    
    return binarysearch(max_budget)

# 그리디
# def greedy(arr):
#     global n
#     arr.sort()
#     def 


# main
n = int(input())
budget = list(map(int, input().split()))
max_budget = int(input())
print(finder(budget))