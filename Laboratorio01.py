from numpy import random

import re

def Board(tablero): #Imprime tablero
    for row in range(len(tablero)):
        print(tablero[row])
    


def Number_Board(tablero, x, y):


    tablero[x].pop(y)
    tablero[x].insert(y, Number_Row[x][y])
    card = Number_Row[x][y]
    Board(tablero)
    return card


def Condition(card1, card2, tablero, x, y): 

    if card1 == card2:
        Numbers.remove(card1)
        tablero[x].pop(y)
        tablero[x].insert(y, "      ")
        
    
    else:
        tablero[x].pop(y)
        tablero[x].insert(y, ("(%d, %d)" % (x, y)))

        print()
        print(Coordinate_Row[x][y])
        print()
 

    
    return tablero
    

Number_cards =int(input("How many cards do you want to play: "))
Pair_of_cards = Number_cards * 2
Board_Row = Pair_of_cards

while Board_Row % 4 != 0:
    Board_Row += 1
print(Board_Row)

Numbers = []  
Number_Row = []
Coordinate_Row = []

print((Board_Row // 4))

for row in range(Board_Row // 4):
    Column_Number = []
    Coordinate_Column = []

    while len(Column_Number) < 4:
        card = random.randint(1, (Number_cards + 1))

        if Numbers.count(card) < 2:
            Numbers.append(card)
            Column_Number.append(card)
            Coordinate_Column.append("(%d, %d)" % (row, len(Column_Number) - 1))

        elif len(Numbers) == Pair_of_cards:
            Column_Number.append("")
            Coordinate_Column.append("      ")

        else:
            continue
        

    Number_Row.append(Column_Number)
    Coordinate_Row.append(Coordinate_Column)

    print(Column_Number) #Borrar

"""
Player_1 = 0
Player_2 = 0
x = 1
d = 0
tablero = Coordinate_Row

while x <= 2:  # len(Numbers)== 0
    
    print("It´s player %d turn:  \n" % (x))
    Board(tablero)
    
        
    coordenada = input("Enter a coordinate:")
    d = re.sub(r"[^\w\s]", "", coordenada) 
    print()
    print(d[0])  # Cambiar coordenadas
    print(d[1])
    x1 = int(d[0])
    y1 = int(d[1])

    card1 = (Number_Board(tablero, x1, y1))
    print()
    print(card1)


    coordenada = input("Enter a coordinate:")
    d = re.sub(r"[^\w\s]", "", coordenada)
    print()
    print(d[0])  # Cambiar coordenadas
    print(d[1])
    x2 = int(d[0])
    y2 = int(d[1])
    card2 = (Number_Board(tablero, x2, y2))
    print()
    print(card2)

    Condition(card1, card2, tablero, x1, y1)
    Condition(card1, card2, tablero, x2, y2)
    Board(tablero)

    if x == 1:
        if card1 == card2:
            Player_1 += 1
        else:
            x += 1
    elif x == 2:
        if card1 == card2:
            Player_2 += 1
        else:
            x -=1
"""  



















































