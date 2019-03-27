N = int(input())
numbers = list(map(int, input().split()))

# 버블정렬 구현(앞에서부터)
for i in range(N-1):
    for j in range(i+1, N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

# # 사실은 이렇게 해도 된다.
# print(*sorted(numbers))