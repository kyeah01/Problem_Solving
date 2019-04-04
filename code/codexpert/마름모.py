n,k = map(int,input().split())
string = list(input())
result = []

for i in range(n//4):
    for i in range(0,n,n//4):
        result += [int(''.join(string[i:i+n//4]), 16)]
    string += [string.pop(0)]

print(sorted(list(set(result)))[-k])