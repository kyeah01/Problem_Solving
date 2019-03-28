def fibo(k, n):
    global arr
    if len(arr) > n:
        return arr[n]
    arr += [arr[k-1] + arr[k-2]]
    return fibo(k+1, n)
    
 
n = int(input())
arr = [0, 1]
print(fibo(2, n))