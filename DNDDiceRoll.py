import random

# Dungeons and Dragons Dice Roll Simulator

def d10():
    x = random.randrange(1, 11)
    return x

def d12():
    y = random.randrange(1, 13)
    return y
    
def d20():
    z = random.randrange(1, 21)
    return z

def dx(x):
    a = random.randrange(1, x+1)
    return a

# Wrapper function that rolls based on input, including a custom-sided dice
def rollDice():
    
    # Control variable for while loop
    rolling = True
    result = 0
    
    while(rolling):
        print('What dice would you like to roll?')
        print('''1. D20
2. D12
3. D10
4. Other (Specify)
5. Quit''')
        roll = input("Please enter the number of your choice: ")
        if roll == "1":
            result = d20()
            print("You rolled: ", result)
        if roll == "2":
            result = d12()
            print("You rolled: ", result)
        if roll == "3":
            result = d10()
            print("You rolled: ", result)
        if roll == "4":
            x = input("Please enter the size of the dice required (e.g. 20 sides would be '20'): ")
            x = int(x)
            result = dx(x)
            print("You rolled: ", result)
        if roll == "5":
            rolling = False
            quit()

rollDice()