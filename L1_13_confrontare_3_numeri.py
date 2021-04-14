A = 5
B = 1
C = 3

if (A > B):
    if (A > C):
        print(f"{A} è maggiore di {B} e {C}")
    else:
        print(f"{C} è maggiore di {A} e {B}")
else:
    if (B > C):
        print(f"{B} è maggiore di {A} e {C}")
    else:
        print(f"{C} è maggiore di {A} e {B}")