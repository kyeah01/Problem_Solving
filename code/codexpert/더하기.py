def sumit(target_number):
    arr = [0]*n
    ans = "NO"
    def permu(k, total):
        nonlocal ans
        if total == target_number:
            ans = "YES"
            return 
        if total > target_number or n == k or sum(numbers[k:]) < target_number-total:
            return
        for i in [1,0]:
            arr[k] = i
            permu(k+1, total+numbers[k]*arr[k])
    permu(0,0)
    return ans

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(sumit(k))