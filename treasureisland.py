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

entrance1 = input("You come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat.Type swim to swim across: ")

if entrance1 == "wait":
    print("You are waiting for something to happen")
elif entrance1 == "swim":
    print("You have been ate by a dragon and killed. Game Over!")

entrance2 = int(input("You suddenly are greeted by a fairy who gives you two options. 50 to enter the island or 100 to skip the island and go to the other side of the lake.Which do you want?: "))

if entrance2 == 50:
    print("You have been teleported to the island ")
if entrance2 == 100:
    print("You have been summoned to hell and killed. Game over!")

age = int(input('You enter the island and collect all the loot. You are greeted by a demon which ask you the question. How old are you mortal? What is your age?'))
if age > 12 and age < 35:
    print(f"So you are {age} years old. I will spare your life since you are still young but never return mortal.")
else:
    print(f"Ahahah so you are {age} years old. Well sucks for becuase ive been craving some old blood. You are killed by the demon. Game over!")



body_part = input("You continue back on your boat and look at your treasure map. You notice a island in the distance which is the same island shown on the map for the treasure.You travel the rest of distance and are treated with vicous waves.You are greeeted by fairy again who gives you two options .You must either cut one arm off or Cut one leg off. So do you want to cut leg off or cut arm off?")

if body_part == "cut leg off":
    if body_part == "leg":
            print("Your leg has been cut off. The waves have suddenly disapeared and you continue in pain to the island.")

if body_part == "cut arm off":
    if body_part == "arm":
            print("The fairy mistakes your arm for head and cuts your head off. You have been killed. Game over.")


ending = input("You reach the island and see the treasure chest under a palm tree. You cry in pain without a leg and open the treasure with your last piece of strength. You look in disbelief and cry as the treasure chest is empty of treausre. But the chest has one thing. A serum...  Do you take the mysterious serum yes or no?:")

if ending == "yes":
    print("You pick up the serum and inject it into yourself. All of the sudden you start seeing white which slowly turns into dark. It was a poison serum. You have died. Game over!")
if ending == "no":
    print("You reject the serum and are greeted by the fairy. The fairy respects your honor and says Congrats you have passed the test! Here is your reward. You are rewarded with your leg back and a full chest of treasure. Congrats YOU WIN THE GAME!")


