from numpy import random
import re

def Board(tablero): #Imprime tablero
    for row in range(len(tablero)):
        #for column in range(len(Coordinate_Column)):
        print(tablero[row])


def Number_Board():
    coordenada = input("Enter a coordinate:")
    d = re.sub(r"[^\w\s]","", coordenada)
    print(d[0]) #Cambiar coordenadas
    print(d[1])
    x = int(d[0])
    y = int(d[1])
    tablero = Coordinate_Row

    tablero[x].pop(y)
    tablero[x].insert(y, Number_Row[x][y])
    Board(tablero)
    """
    tablerofi = []
    for row in range(len(Coordinate_Row)):
        tablerocol = []
        for column in range(len(Coordinate_Column)):
            if row == int(x[0]) and column == int(x[1]):
                tablerocol.append(Number_Row[row][column])

            else:
                tablerocol.append(Coordinate_Row[row][column])
        print(tablerocol)
    """

Number_cards = 8 #int(input("How many cards do you want to play: "))
Pair_of_cards = Number_cards * 2


Coordinate_Row = []  
Numbers = []  
Number_Row = []

for row in range(4):
    Coordinate_Column = []
    Column_Number = []

    while len(Column_Number) <= 3:
        card = random.randint(1, 9)

        if Numbers.count(card) < 2:
            Coordinate_Column.append("(%d, %d)" % (row, len(Column_Number)))

            Numbers.append(card)
            Column_Number.append(card)
        else:
            continue

    Number_Row.append(Column_Number)
    Coordinate_Row.append(Coordinate_Column)
    
    print(Coordinate_Column, Column_Number)

print()

Player_1 = 0
Player_2 = 0
x = 0
while x == 0:  # len(Numbers)== 0
    if x == 0:
        print("It´s player 1 turn:  \n")
        Board(Coordinate_Row)
        Number_Board()

        x += 1
    """
    elif x == 1:
        print("It´s player 2 turn:  \n")
        board()
        x -= 1
    """
    





















































