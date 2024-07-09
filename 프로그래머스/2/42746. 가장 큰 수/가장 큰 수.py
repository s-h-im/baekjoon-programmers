def solution(numbers):

    arr = [str(num) for num in numbers]  
    arr.sort(key = lambda num : num * 3, reverse = True) 

    return str(int(''.join(arr)))