def solution(array, commands):
    answer = []
    for row in commands:
        temp = array[row[0] - 1:row[1]]
        temp.sort()
        answer.append(temp[row[2] - 1])
    return answer