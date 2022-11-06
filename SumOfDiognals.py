def diognal():
    arr = [[1, 2, 3], 
            [4, 5, 6], 
            [9, 8, 9]]

    i, j = 0, 0
    sum1, sum2 = 0, 0

    while i < 3:
        sum1 += arr[i][j]
        j += 1
        i += 1

    x, y = 0, 2  

    while x < 3:
        sum2 += arr[x][y]
        x += 1
        y -= 1

    diff = sum1 - sum2

    if diff < 0:
        diff *= -1

    return diff



print(diognal()) 