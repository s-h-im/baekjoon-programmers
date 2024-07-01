def solution(s):
    answer = True
    s = list(s)
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) > 0 and (stack[-1] == '(' and s[i] == ')'): 
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) > 0:
        answer = False
    return answer