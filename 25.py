import numpy as np
import random
import operator

#Bekérem az inputokat
n = int(input("Kérem adja meg a számot: "))
size = int(input("Kérem adja meg a vektor méretét: "))
interval = input("Kérem adja meg az intervallumot (pl. 1-100): ")

#Darabolom a stringet "-" szerint, majd átváltom intre.
rng = interval.split("-")
rng[0] = int(rng[0])
rng[1] = int(rng[1])

#Létrehozom a véletlenszerű műveleti jeleket
def randomOperato():
    operators = ['+','-','*','/']
    op = random.choice(operators)
    return op

def expressionMake(v):
    prime_numbers, even_numbers, odd_numbers = [],[],[]
    #Prím számok
    for i in range(len(v)):
        if v[i] > 1:
            for j in range(2,v[i]):
                if (v[i] % j) == 0:
                    break
                else:
                    prime_numbers.append(v[i])

    for i in range(len(v)):