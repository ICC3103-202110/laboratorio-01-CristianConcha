from numpy import random

import re

def Board(tablero): #Imprime tablero
    for row in range(len(tablero)):
        print(tablero[row])
    print()


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
    


            
Number_cards =int(input("How many cards do you want to play: "))
Pair_of_cards = Number_cards * 2
Board_Row = Pair_of_cards

while Board_Row % 4 != 0: #Board Dimensions 
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


Player_1 = 0
Player_2 = 0
x = 1
tablero = Coordinate_Row

while len(Numbers) >= 1:  
    print("It´s player %d turn:  \n" % (x))
    Board(tablero)
    
        
    coord_x = int(input("Enter coordinate x: "))
    coord_y = int(input("Enter coordinate y: "))
    print(coord_x, coord_y)
    card1 = (Number_Board(tablero, coord_x, coord_y))
    print()
    print(card1)

    coord_x2 = int(input("Enter coordinate x: "))
    coord_y2 = int(input("Enter coordinate y: "))
    print(coord_x2, coord_y2)
    card2 = (Number_Board(tablero, coord_x2, coord_y2))
    print()
    print(card2)

    Condition(card1, card2, tablero, coord_x, coord_y)
    Condition(card1, card2, tablero, coord_x2, coord_y2)
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
            x -= 1

    if len(Numbers) == 0:
        if Player_1 > Player_2:
            print("Player 1 win, with %d points" % (Player_1))
        elif Player_1 < Player_2:
            print("Player 2 win, with %d points" % (Player_2))
        elif Player_1 == Player_2:
            print("Tie between player 1 and player 2, with  %d points" %(Player_1))


















































