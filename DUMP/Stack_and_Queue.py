from collections import deque

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

top = stack.pop()
print(top)

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q.popleft())