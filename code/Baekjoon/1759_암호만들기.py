def howMany(arr):
    cnt = 0
    for x in arr:
        if x in 'aeiou':
            cnt += 1
    if cnt >= 1 and len(arr)-cnt>=2:
        return True
    return False

def permu(L, k, ans):
    if k == L:
        if howMany(ans):
            result.append(''.join(ans))
        return
    for i in alphas:
        if i not in ans[:k]:
            if k==0 or ord(ans[k-1]) < ord(i):
                ans[k] = i
                permu(L, k+1, ans)

L, C = map(int, input().split())
alphas = input().split()
ans = ['' for _ in range(L)]
result = []
permu(L, 0, ans)
for r in sorted(list(set(result))):
    print(r)