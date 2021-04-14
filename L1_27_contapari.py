numeri = [12,23,43,5,6,7,34,5,46,76,9]
#numero da cercare
conteggio = 0

for el in numeri:
    print(el, end=' ')
    if ((el % 2) == 0):
        conteggio += 1    

print("\nnumeri pari: ", conteggio)
    
