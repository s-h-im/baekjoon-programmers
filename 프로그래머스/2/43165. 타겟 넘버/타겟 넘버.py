from collections import deque

def solution(numbers, target):
    q = deque([0])
    for n in numbers:
        for _ in range(len(q)):
            x = q.popleft()
            q.append(x + n)
            q.append(x - n)
    return q.count(target)