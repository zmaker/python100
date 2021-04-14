numeri = [12, 23, 34, 45, 56]

i = 1
for x in numeri:
    if ( i < len(numeri)): 
        print(x, end=", ")
    else:
        print(x)
    i += 1