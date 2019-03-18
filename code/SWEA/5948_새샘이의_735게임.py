# 차라리 조합을 구해서 sort를 하자
def combination(arr):
    ans = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                ans += [arr[i]+arr[j]+arr[k]]
    return sorted(list(set(ans)))

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(combination(numbers)[-5])