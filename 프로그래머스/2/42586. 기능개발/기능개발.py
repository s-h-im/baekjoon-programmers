import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    d = deque()
    for i in range(len(progresses)):
        d.append(math.ceil((100 - progresses[i]) / speeds[i]))
    while len(d) > 0:
        first = d.popleft()  
        cnt = 1
        while len(d) > 0 and first >= d[0]:
            d.popleft()
            cnt += 1      
        answer.append(cnt)
    return answer