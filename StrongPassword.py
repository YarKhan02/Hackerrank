def password():
    p = '2bbbb'
    s = '!@#$%^&*()-+'
    c1, c2, c3, c4 = 0, 0, 0, 0

    for i in p:
        if (ord(i) >= 65) and (ord(i) <= 90):
            c1 = 0
            c1 += 1
        elif(ord(i) >= 48) and (ord(i) <= 57):
            c2 = 0
            c2 += 1
        elif(ord(i) >= 97) and (ord(i) <= 122):
            c3 = 0
            c3 += 1
        else:
            for j in s:
                if (ord(i) == ord(j)):
                    c4 = 0
                    c4 += 1

    count = c1 + c2 + c3 + c4

    return max(6 - len(p), 4 - count) 

print(password())