import random
segreto = random.randint(1, 10)
print('indovina il numero')
risposta = 0

while not(risposta == segreto):
    risposta = int(input("che numero? "))

print('esatto!')