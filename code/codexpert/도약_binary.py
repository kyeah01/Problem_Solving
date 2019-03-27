def polzzak(arr):
    global n
    
    def binary_search():
        nonlocal n
        s, e = 0, n
        while s 
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            # first_leap = arr[i]
            # second_leap = arr[j]
            first_jump = arr[j] - arr[i]
            # 찾아야 하는 값의 범위는 second_leap + first_jump ~ second_leap + first_jump*2


n = int(input())
lotus = [int(input()) for _ in range(n)]
lotus.sort()



def upperSearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data:
            s = m+1
            sol = m
        else:
            e = m-1
    return sol