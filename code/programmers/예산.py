def check(maxValue, budgets, total):
    temp = 0
    for bud in budgets:
        temp += min(bud, maxValue)
    if total > temp:
        return 1
    elif total == temp:
        return 2
    else:
        return 3

def binarySearch(start, end, budgets, total):
    flag = start
    while start < end:
        mid = (start + end) // 2
        checkValue = check(mid, budgets, total)
        if checkValue == 1:
            start = mid + 1
            flag = start
        elif checkValue == 2:
            return mid
        else:
            end = mid - 1
            flag = end
    if check(flag, budgets, total) == 1:
        return flag
    elif check(flag, budgets, total) == 2:
        return flag + 1
    return flag - 1

def solution(budgets, M):
    if M >= sum(budgets):
        return max(budgets)
    return binarySearch(0, max(budgets), budgets, M)
