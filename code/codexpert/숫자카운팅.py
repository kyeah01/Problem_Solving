def binary_search(target_number, arr):
    def binary_search_lower():
        nonlocal target_number, arr
        s, e = 0, len(arr)
        sol = -1
        while s <= e:
            mid = (s+e)//2
            if arr[mid] < target_number:
                s = mid+1
            # 만약에 똑같으면?
            elif arr[mid] == target_number:
                sol = mid
                e = mid-1
            else:
                e = mid-1
        return sol

    def binary_search_upper():
        nonlocal target_number, arr
        s, e = 0, len(arr)
        sol = -1
        while s <= e:
            mid = (s+e)//2
            if arr[mid] > target_number:
                e = mid-1
            elif arr[mid] == target_number:
                sol = mid
                s = mid+1
            else:
                s = mid+1
        return sol
    
    lower = binary_search_lower()
    if lower != -1:
        upper = binary_search_upper()
        return upper-lower+1
    return 0

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target_numbers = list(map(int, input().split()))
print(*list(binary_search(target_number, arr) for target_number in target_numbers))