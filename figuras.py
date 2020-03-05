

def figurinhas(c, m):
    cx = [4,2]
    my = [7,1,8,4,9,3]

    for i in range(c):
        for x in range(m):
            if cx[i] == my[x]:
                c = c-1
    return c
