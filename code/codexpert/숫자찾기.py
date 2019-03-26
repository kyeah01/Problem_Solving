def binary_finder(target_number, start, end):
    if start == end:
        return 0
    if arr[(start+end)//2] == target_number:
        return (start+end)//2
    # 비교하는 값보다 타겟이 작다면, 프론트로 가야함.
    elif arr[(start+end)//2] > target_number:
        return binary_finder(target_number, start, (start+end)//2)
    else:
        return binary_finder(target_number, (start+end)//2, end)

n = int(input())
arr = list(map(int, input().split()))
count = int(input())
target_number = list(map(int, input().split()))

for i in range(count):
    print(binary_finder(target_number[i], 0, n))