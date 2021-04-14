import random

print('cerca il numero')

#genero una lista di 30 numeri casuali
numeri = []
n = 30
while (n > 0):
    n -= 1
    r = random.randint(0,100)
    numeri.append(r)

ripeti = True
while(ripeti):
    src = int(input("Che numero?"))
    trovato = False
    
    trovato = False
    i = 0
    while not trovato and i < len(numeri):
        el = numeri[i]
        if src == el:
            trovato = True 
        i += 1
    
    if trovato:
        print('trovato!')
    else:
        print('non trovato!')
        
print('END')
        

