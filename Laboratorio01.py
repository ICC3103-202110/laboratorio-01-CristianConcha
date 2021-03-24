from numpy import random

def Print_Board(Game_Board):  # Print Board
    for row in range(len(Game_Board)):
        for column in range(4):
            print(Game_Board[row][column], end=" ")
        print()
    print()

def Number_Board(Game_Board, x, y): #Insert number and coordinate in Board
                                                          
    Game_Board[x].pop(y)
    Game_Board[x].insert(y, ("  % d  " % (Number_Row[x][y])))
    card = Number_Row[x][y]
    Print_Board(Game_Board)
    return card


def Condition(card1, card2, Game_Board, x, y): #Correct card or not

    if card1 == card2:
        Numbers.remove(card1)
        Game_Board[x].pop(y)
        Game_Board[x].insert(y, "      ")
        Coordinate_Data.remove(("(%d, %d)" % (x, y)))
        
    else:
        Game_Board[x].pop(y)
        Game_Board[x].insert(y, ("(%d, %d)" % (x, y)))


Number_cards =int(input("How many cards do you want to play: "))
Pair_of_cards = Number_cards * 2
Board_Row = Pair_of_cards

while Board_Row % 4 != 0: #Board Dimensions 
    Board_Row += 1

Numbers = []  
Number_Row = []
Coordinate_Row = []
Coordinate_Data = [] #Total coordinate

for row in range(Board_Row // 4): 
    Column_Number = []
    Coordinate_Column = []

    while len(Column_Number) < 4:
        card = random.randint(1, (Number_cards + 1))

        if Numbers.count(card) < 2:
            Numbers.append(card)
            Column_Number.append(card)
            Coordinate_Data.append("(%d, %d)" %(row, len(Column_Number) - 1))
            Coordinate_Column.append("(%d, %d)" % (row, len(Column_Number) - 1))

        elif len(Numbers) == Pair_of_cards:
            Column_Number.append("")
            Coordinate_Column.append("      ")

        else:
            continue
        
    Number_Row.append(Column_Number)
    Coordinate_Row.append(Coordinate_Column)



Player_1 = 0
Player_2 = 0
Turn = 1
Game_Board = Coordinate_Row

while len(Numbers) >= 1:  
    print("It´s player %d turn:  \n" % (Turn))
    Print_Board(Game_Board)
    
    Great_Input = 0
    while Great_Input == 0:  
        coord_x = int(input("Enter coordinate x: "))
        coord_y = int(input("Enter coordinate y: "))

        if (coord_x < (len(Game_Board)) and ((coord_y < 4))):  # Corroborate the coordinate 1 input
            if ("(%d, %d)" % (coord_x, coord_y)) in Coordinate_Data: # Corroborate if the coordine was used

                card1 = (Number_Board(Game_Board, coord_x, coord_y))
                Great_Input += 1

            else:
                print("The current coordinate has already been used or not exist \n")

        else:
            print("Coordinate number not valid \n")


    while Great_Input == 1: 
        coord_x2 = int(input("Enter coordinate x: "))
        coord_y2 = int(input("Enter coordinate y: "))
    
        if (coord_x2 < (len(Game_Board)) and ((coord_y2 < 4))):  # Corroborate the coordinate 2 input
            if ("(%d, %d)" % (coord_x2, coord_y2)) in Coordinate_Data: # Corroborate if the coordine was used

                card2 = (Number_Board(Game_Board, coord_x2, coord_y2))
                Great_Input += 1

            else:
                print("The current coordinate has already been used or not exist \n")

        else:
            print("Coordinate number not valid \n")

    
    Condition(card1, card2, Game_Board, coord_x, coord_y)
    Condition(card1, card2, Game_Board, coord_x2, coord_y2)

    if Turn == 1: # Players score
        if card1 == card2:
            Player_1 += 1
        else:
            Turn += 1
    elif Turn == 2:
        if card1 == card2:
            Player_2 += 1
        else:
            Turn -= 1

    if len(Numbers) == 0: # Win player
        if Player_1 > Player_2:
            print("Player 1 win, with %d points" % (Player_1))

        elif Player_1 < Player_2:
            print("Player 2 win, with %d points" % (Player_2))

        elif Player_1 == Player_2:
            print("Tie between player 1 and player 2, with  %d points" %(Player_1))


















































