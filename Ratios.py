def ratio():
    arr = [1, 1, 0, -1, -1]
    p, n, z = 0, 0, 0
    l = len(arr)

    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1

    p = p/l
    print(p)
    n = n/l
    print(n)
    z = z/l 
    print(z)

print(ratio())
    
