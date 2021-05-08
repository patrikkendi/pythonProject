import numpy as np
import operator
import random

n = int(input('Type in a number: '))
size = int(input('Type in the size of the vector: '))
start = int(input('Type in the start of the interval: '))
stop = int(input('Type in the end of the interval: '))

#Véletlenszerű műveleti jeleket generáló függvény
def randomOperator():
    ops = ['+', '-', '*', '/']
    op = random.choice(ops)
    return op


def expressionMake(v):
    prime_numbers, even_numbers, odd_numbers = [], [], []

    # megnézzük, mely számok prímek
    for i in range(len(v)):
        if v[i] > 1:
            for j in range(2, v[i]):
                if (v[i] % j) == 0:
                    break
            else:
                prime_numbers.append(v[i])
    #megnézzük mely számok párosak, páratlanak, prímek és hozzáadjuk a listához
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

#Ez a függvény a kapott listán végig iterál, majd hozzáadja a kapott jeleket és megoldja azt
def expressionSolve(iterable):

    expression = ''
    for i in range(len(iterable)):
        operation_string = randomOperator()
        if i == len(iterable) - 1:  # mert nem kell operator az utolso elem után
            expression += f'{iterable[i]}'
        else:
            expression += f'{iterable[i]} {operation_string} '

    result = str(eval(expression))

    return f'{expression} = {result}'


for i in range(n):
    v = np.random.randint(start, stop, size)

    exp_type, exp = expressionMake(v)

    print(f'{i + 1}. ({exp_type}) {expressionSolve(exp)}')