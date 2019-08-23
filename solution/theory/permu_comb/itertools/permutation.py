import itertools

arr = [1,2,3]

print(itertools.permutations(arr))

# 그냥 itertools.permutations는 
# <itertools.permutations object at 0x00000263AF8C6EB8>
# 객체 순환해서 출력하는 결과를 만들어야 한다.
print([i for i in itertools.permutations(arr)])

# permutations는 다른 인자도 받을 수 있다.
# 해당 arr 뒤에 arr 갯수 이하의 값을 줘서 원하는 갯수의 인자를 가지는 순열을 찾을 수 있다.
print([i for i in itertools.permutations(arr, 3)])


# 따라서 arr가 가질 수 있는 모든 인자개수, 모든 경우의 순열을 구하려고 한다면,
for i in range(len(arr)+1):
    print([j for j in itertools.permutations(arr, i)])