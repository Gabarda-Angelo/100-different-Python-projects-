print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


left_right = input('you\'re at a cross road where do you want to go?'
                   'Type "left" or "right"\n').lower()



if left_right == "left":
    wait_swim= input('You\'ve come to a lake. '
                     'There is an island in the middle of the lake '
                     'Type "wait" to wait for a boat. '
                     'Type "swim" to swim across\n').lower()
    if wait_swim == "wait":

        red_yellow_blue = input('You arrive at the island unharmed. '
                                'There is a house with 3 doors.One "red", one "yellow" and one "blue". '
                                'Which colour do you choose?\n').lower()
        if red_yellow_blue == "yellow":
            print("YOU WIN CONGRATS!")
        elif red_yellow_blue == "blue":
            print("eaten by beasts roar! GAME OVER!")
        elif red_yellow_blue == "red":
            print("Burned by fire Game over!")
    elif wait_swim == "swim":
        print("attack by trout. GAME OVER!")

elif left_right.lower == "right":
    print("Fall into a hole. GAME OVER!")
