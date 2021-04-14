numeri = [12,23,43,5,6,7,34,5,46,76,9]
#numero da cercare
chiave = 7

for el in numeri:
    print(el, end=', ')
    if (chiave == el):
        print(f"trovato {chiave}")
        print("stop")
        break
    