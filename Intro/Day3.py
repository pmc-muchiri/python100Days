print('''      ____
                  /^\   / -- )
                 / | \ (____/
                / | | \ / /
               /_|_|_|_/ /
                |     / /
 __    __    __ |    / /__    __    __
[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ]
|__            ____/ /___           __|
   |          / .------  )         |
   |         / /        /          |  SheDragon
   |        / /        /           |
~~~~~~~~~~~~-----------~~~~~~~~ldb~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
print("Welcome to Treasure ISLAND OF PAUL AND JUDY")
choice_1 = input("Choose which way to take Left or Right?:\n").lower()
if choice_1 == 'left':
    choice_2 = input("Swim or wait?:\n")
    if choice_2 == 'wait':
        choice_3= input("Which door? Blue, Red or Yellow:\n").lower()
        if choice_3 =='red' and 'blue':
            print("GAME OVER!!! You got burnt?:\n")
        elif choice_3 == 'yellow':
            print("YOU WIN!!!!!!")
        else:
            print("GAME OVER!!! Make sure you read instructions well")
    else:
        print("GAME OVER!!! You drown")

else:
    print("GAME OVER!!! You have fall in to a hole")
