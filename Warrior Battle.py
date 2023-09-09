import os, time, random

def diceRoll(sides):
    roll = random.randint(1, sides)
    return roll

def hp():
    health = ((diceRoll(6) * diceRoll(12)) / 2) + 10
    return health

def str():
    strength = ((diceRoll(6) * diceRoll(12)) / 2) + 10
    return strength


print("BATTLE TIME!")
print()
c1Name = input("Name your Legend: ")
c1CharType = input("Choose your type: Human, Elf, Wizard, Orc ")
c1Health = hp()
c1Strength = str()
print(c1Name, c1CharType)
print(f"HP:{c1Health}")
print(f"STR: {c1Strength}")
print()
time.sleep(1.5)
print("Who are they battling?")
print()
c2Name = input("Name your Legend: ")
c2CharType = input("Choose your type: Human, Elf, Wizard, Orc ")
c2Health = hp()
c2Strength = str()
print(c2Name, c2CharType)
print(f"HP:{c2Health}")
print(f"STR: {c2Strength}")

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("cls")
    c1Dice = diceRoll(6)
    c2Dice = diceRoll(6)
    damage = abs(c1Health - c2Health) + 1

    if c1Dice > c2Dice:
        c2Health -= damage
        round += 1
        if round == 1:
            print(c1Name, "has won the first round!")
        else:
            print(c1Name, "has won the round!")
    elif c2Dice > c1Dice:
        c1Health -= damage
        round += 1
        if round == 1:
            print(c2Name, "has won the first round!")
        else:
            print(c2Name, "has won the round!")
    else:
        print(c1Name, "and", c2Name, "have drawn.")
    print()
    print(c1Name)
    print(f"HP: {c1Health}")
    print()
    print(c2Name)
    print(f"HP: {c2Health}")
    
    if c1Health <= 0:
        print(c1Name, "has fallen!")
        winner = c2Name
        break
    elif c2Health <= 0:
        print(c2Name, "has fallen!")
        winner = c1Name
        break
time.sleep(1)
os.system("cls")
print(winner, "has won in", round, "rounds")
