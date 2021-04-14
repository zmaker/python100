domande = [
    'Quale di queste affermazioni '\
    'sulla balena è sbagliata?',
    'Che cos\'è l\' \"abacà\", il primo sostantivo in un dizionario italiano?',
    'Se da San Francisco vedete il famoso "Golden Gate" cosa state guardando?'
    ]
scelte = [
    ['ha i fanoni', 'è un cetaceo',
     'ha 2 figli per volta', 'si nutre di krill'],
    ['un liquore', 'la parte di un libro',
     'una fibra tessile', 'una veste romana'],
    ['un grattacielo', 'un ponte',
     'un lago', 'un monte']
    ]
risposte = [3, 3, 2]

punti = 0
idom = 0
for dom in domande:
    print(dom)
    c = 1
    for cho in scelte[idom]:
        print(f"{c}: {cho}")
        c += 1
    ans = int(input("1, 2, 3 o 4? "))
    
    right = risposte[idom]
    if (right == ans):
        print("corretto!\n")
        punti += 1
    else:
        print("non è corretto!\n")
    
    idom += 1
    
print(f"Il tuo punteggio: {punti}")
