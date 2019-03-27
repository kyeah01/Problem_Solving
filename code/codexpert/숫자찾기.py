# def binary_search(s,e, target_number):
#     mid = (s+e)//2
#     if target_number == arr[mid]:
#         return mid+1
#     if s >= e:
#         return 0
#     if target_number < arr[mid]:
#         return binary_search(s, mid, target_number)
#     if target_number > arr[mid]:
#         return binary_search(mid+1, e, target_number)

def binary_search(s,e, target_number):
    while s < e:
        mid = (s+e)//2
        if target_number == arr[mid]:
            return mid+1
        elif target_number < arr[mid]:
            e = mid
        else:
            s = mid+1
    return 0

n = int(input())
arr = list(map(int, input().split()))
count = int(input())
target_numbers = list(map(int, input().split()))

for target_number in target_numbers:
    print(binary_search(0, n, target_number))