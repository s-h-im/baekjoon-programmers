def solution(sizes):
    for row in sizes:
        row.sort(reverse = True)
    sizes.sort(reverse = True)
    a = sizes[0][0]
    b = 0
    for row in sizes:
        if b < row[1]:
            b = row[1]
    return a * b