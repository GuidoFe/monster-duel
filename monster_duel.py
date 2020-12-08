import random

A = ((3, 100),)
B = ((2, 56), (4, 22), (6, 22))
C = ((1, 51), (5, 49))


current = A

def getRandom(hero):
    if hero == "A":
        return 3
    elif hero == "B":
        return random.choices(population=[2,4,6], weights=[56,22,22])[0]
    elif hero == "C":
        return random.choices(population=[1,5], weights=[51,49])[0]

def round1(hero):
    opponents = ["A", "B", "C"]
    opponents.remove(hero)
    return(getRandom(hero)>getRandom(random.choices(opponents)[0]))

def round2(hero):
    opponents = ["A", "B", "C"]
    opponents.remove(hero)
    roll = getRandom(hero)
    return (roll > getRandom(opponents[0]) and roll > getRandom(opponents[1]))

rounds = 0
none = 0
heros = {"A": 0, "B": 0, "C": 0}
while rounds < 1000000:
    for hero in heros:
        if round1(hero) and round2(hero):
            heros[hero] += 1
    rounds += 1
    print("##############################")
    print("Round " + str(rounds))
    print("A = "+str(heros["A"]/rounds))
    print("B = "+str(heros["B"]/rounds))
    print("C = "+str(heros["C"]/rounds))
