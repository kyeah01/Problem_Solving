import collections

d = collections.deque([1,2,3,4,5])
d.append(5)
print(d)

d = collections.deque([1,2,3,4,5])
d.appendleft(1)
print(d)

d = collections.deque([1,2,3,4,5])
print(d.pop())
print(d)

d = collections.deque([1,2,3,4,5])
d.rotate(1)
print(d)
