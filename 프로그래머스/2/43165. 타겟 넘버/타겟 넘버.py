from collections import deque

def solution(numbers, target):
    result = 0
    dq = deque()  
    dq.append((numbers[0], 1)) 
    dq.append((-numbers[0], 1))
    while dq:  
        x = dq.popleft()  
        if x[1] == len(numbers):
            if x[0] == target:    
                result += 1
        else:
            dq.append((x[0] + numbers[x[1]], x[1] + 1))  
            dq.append((x[0] - numbers[x[1]], x[1] + 1))  
    return result
