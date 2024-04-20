print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

first_riddle = input("You're at a cross road. Which way you wanna go ? left or right\n")
if first_riddle == "left":
  print("You have now reached the lake. Do you wanna wait for the boat or swim across the lake? [Type wait or swim]")
  second_riddle = input()
  if second_riddle == "wait":
    print("You've now reached near Castle, Which Door Do You Wanna Go In? red, blue, yellow?")
  else:
    print("Attacked by trout.\nGame Over!")
  third_riddle = input()
  if third_riddle == "yellow":
    print("Hooray! You found the Treasure")
  elif third_riddle == "blue":
    print("Eaten by Beasts.\nGame Over!")
  elif third_riddle == "red":
    print("Burned by fire.\nGame Over!")  
else:
  print("Whoops! You fell in a Hole\nGame Over!")

