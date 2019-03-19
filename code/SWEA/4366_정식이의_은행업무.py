def mybin(arr):
    return sum(2**i for i in range(len(arr)) if int(arr[::-1][i]))

def mytetra(arr):
    return sum(int(arr[::-1][i])*3**i for i in range(len(arr)) if int(arr[::-1][i]))

# 또는 int()

def finder(two, three):
    for j in range(len(two)):
        second = list(two)
        second[j] = 0 if int(second[j]) else 1
        for i in range(len(three)):
            third = list(three)
            if int(third[i]) == 2:
                third[i] = 0
                if mybin(second) == mytetra(third):
                    return mybin(second)
                third[i] = 1
                if mybin(second) == mytetra(third):
                    return mybin(second)
            elif int(third[i]) == 1:
                third[i] = 0
                if mybin(second) == mytetra(third):
                    return mybin(second)
                third[i] = 2
                if mybin(second) == mytetra(third):
                    return mybin(second)
            else:
                third[i] = 1
                if mybin(second) == mytetra(third):
                    return mybin(second)
                third[i] = 2
                if mybin(second) == mytetra(third):
                    return mybin(second)

T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()
    print(finder(two, three))
    # print(mybin(two))
    # print(mytetra(three))