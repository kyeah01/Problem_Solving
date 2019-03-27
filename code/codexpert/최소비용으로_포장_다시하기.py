N = int(input())
candys = list(map(int, input().split()))

# # 1.
# # min을 찾아서 뽑아내는 경우.
# total = 0
# while len(candys) > 1:
#     price = candys.pop(candys.index(min(candys))) + candys.pop(candys.index(min(candys)))
#     total += price
#     candys += [price]

# print(total)

# # 2.
# # 처음에 정렬해서 가장 작은 것을 찾아서 포장한다.
# # 다음, 버블소트를 2회전시켜서 가장 작은 두개가 앞으로 올때까지 정렬한다.
# # 하나만 남을때까지 계속한다.

# def inboxing(arr):
#     global N, candys
#     arr.sort()
#     def BubbleSort(arr, times):
#         N = len(arr)
#         for i in range(times):
#             for j in range(i+1, N):
#                 if arr[i] > arr[j]:
#                     arr[i], arr[j] = arr[j], arr[i]
#         return arr
#     total_price = 0
#     while len(candys) >= 2:
#         price = candys.pop(0) + candys.pop(0)
#         total_price += price
#         candys += [price]
#         candys = BubbleSort(candys, 2)
#     return total_price

# print(inboxing(candys))


# 3. insert 정렬하기
# 

def inboxing(arr):
    global N, candys
    arr.sort()
    
    def InsertSort(arr, item):
        N = len(arr)
        for i in range(N):
            if arr[i] >= item:
                arr.insert(i, item)
                break
        else:
            arr += [item]
        return arr

    total_price = 0
    while len(candys) >= 2:
        price = candys.pop(0) + candys.pop(0)
        total_price += price
        candys = InsertSort(candys, price)
    return total_price

print(inboxing(candys))