from collections import deque
import sys
q = deque()
n = int(input())

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push_front':
        q.appendleft(s[1])
    elif s[0] == 'push_back':
        q.append(s[1])
    elif s[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[len(q) - 1])
        else:
            print(-1)