numeri = [10, 20, 14]
nomi = ["Paolo", "Mario", "Anna"]

mista = [2, 'mele', 2.4, 4, 'banane', 0.99]

#numero di elementi
n = len(numeri)
print("la lista contiene", n, "elementi")

# stampo o estraggo un elemento
print(numeri[0])

#stampo la lista:
print(numeri)
print(nomi)

#Come sostituisco il valore di un elemento?
print(numeri)
numeri[1] = 99
print(numeri)

#creo liste vuote
myList = []
print("Una lista vuota: ")
print(myList)
  
#aggiungo elementi
myList.append(1)
print(myList)

#aggiungo una lista a una lista
elenco = ['foo', 'bar']
myList.append(elenco)
print(myList)
  
#inseriamo un elemento
numeri = [1,2,3,4]
print("Elenco iniziale: ", numeri)
#aggiungo l'elemento 12 alla pos. 3.
numeri.insert(3, 12)
print(numeri)

#inserire più elementi alla fine della lista con extend():
numeri.extend([100, 200, 300])
print("Lista estesa: ", numeri)


#Per rimuovere un elemento usiamo remove(elemento)
numeri.remove(2)
print("ho rimosso l'elemento '2': ", numeri)

spesa = ['mele', 'pane', 'salame']
print(spesa)
spesa.remove('pane')
print(spesa)


#rimuovere l’ultimo elemento con pop()  
numeri.pop()
print("Rimuovo l'ultimo elemento:")
print(numeri)
#pop usa anche un indice
numeri.pop(2)
print("rimuovo l'elemento alla pos. 2: ")
print(numeri)

#Si possono creare anche delle liste a due dimensioni:
matrice = [[10,20.30,40] , [11,22,33,44]]
print(matrice)

#Prendere delle parti di una lista (slicing):
numeri = [12, 23, 34, 45, 56, 67, 78, 89]
print("lista di partenza")
print(numeri)
lista2 = numeri[3:5]
print("parte della lista originale (sliced list):")
print(lista2)
  
lista3 = numeri[:2]
print(lista3)

lista4 = numeri[5:]
print(lista4)


