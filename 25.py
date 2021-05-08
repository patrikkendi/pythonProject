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
def randomOperator():
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

    #Megnézem hogy a szám páros e vagy páratlan
    for i in range(len(v)):
        if (v[i] % 2) == 0:
            even_numbers.append(v[i])
        else:
            odd_numbers.append(v[i])

    if len(prime_numbers) > 1:
        return 'prime_numbers', prime_numbers
    elif len(odd_numbers) > 1:
        return 'odd_numbers', odd_numbers
    else:
        return 'even_numbers', even_numbers

#Létrehozom azt a függvényt,
#mely a kapott listán végig iterál, hozzáad egy random operátort,
#majd megoldja a kifejezést
def expressionSolve(iterable):

    expression = ''
    for i in range(len(iterable)):
        operation_string = randomOperator()
        if i == len(iterable)-1: #Mivel az utolsó után nemkell operátor
            expression += f'{iterable[i]}'
        else:
            expression += f'{iterable[i]} {operation_string}'

