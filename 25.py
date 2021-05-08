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

