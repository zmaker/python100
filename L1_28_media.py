n = int(input("quanti numeri? "))
somma = 0
for i in range(n):
    num = int(input("numero? "))
    somma += num

media = somma / n
print("la media è: ", media)

