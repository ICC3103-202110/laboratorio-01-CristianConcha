from numpy import random

Number_cards = 8 #int(input("How many cards do you want to play: "))
Pair_of_cards = Number_cards * 2


Fila = [] #coordenadas
coordenada_x = 0
for fila in range(4):
    Columna = []
    coordenada_y = 0
    for columna in range(4):
        Columna.append("(%d, %d)" %(coordenada_x, coordenada_y))
        coordenada_y += 1
    Fila.append(Columna)
    coordenada_x += 1
    
    print(Columna)

print(Fila[3][3])
print()

numeros =[] #numeros aleatorios
Filanum = []

while len(Filanum) <= 4:
    Columnanum = []

    while len(Columnanum) <= 4:
        card = random.randint(1, 9)
        if numeros.count(card) < 2:
            numeros.append(card)
            Columnanum.append(card)
        else:
            continue
    Filanum.append(Columnanum)

    print(Columnanum)
print(numeros.count(3))
print("jedjvciecjoiew")
print(Filanum[3][3])
















































