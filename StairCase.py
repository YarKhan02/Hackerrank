def stair():
    n = 5
    x = n - 1
    i = 0

    while i < n:
        j = 0
        while j < x:
            print(' ', end = '')
            j += 1

        k = 0

        while k <= i:
            print("#", end = '')
            k += 1

        print('')

        i += 1
        x -= 1

print(stair())
