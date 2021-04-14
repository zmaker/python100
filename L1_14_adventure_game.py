print("Sei in una foresta magica e il sole sta tramontando.")
print("Da che parte vai?")
move = input("N, S, E, W? ")

if (move == 'N'):
    print('sei uscito dalla foresta')
elif (move == 'S'):
    print('la foresta ti circonda ancora')
elif (move == 'E'):
    print('tra gli alberi appare una capanna')
elif (move == 'W'):
    print('un lupo ti assale')
else:
    print('Non ho capito dove vuoi andare')
