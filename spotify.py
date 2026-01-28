def men(i, limit):
    if i > limit:
        return
    print(i)
    men(i+1,limit)
men(0, 5)
#recussion