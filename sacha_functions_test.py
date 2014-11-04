__author__ = 'sacha'


from math import *
import re

def main():

    keep_going = "y"
    while keep_going == "y":
        print(eval(input("Please a command to receive information about your function: ")))
        keep_going = input("Do you want to continue? (y/n)")



def val(function, x):
    return eval(function)


def min_val(function, x1, x2):
    x = x1
    min_value = eval(function)

    for x in range(x1 + 1, x2 + 1):
        if eval(function) < min_value:
            min_value = eval(function)

    return min_value


def max_val(function, x1, x2):
    x = x1
    max_value = eval(function)

    for x in range(x1 + 1, x2 + 1):
        if eval(function) > max_value:
            max_value = eval(function)

    return max_value


def area(function, x1, x2):
    area = 0

    for x in range(x1, x2):
        area += (x + 1 - x) * (val(function, x) + val(function, x + 1)) / 2

    return area


def root(function, x1, x2):
#Pour le moment la cette fonction ne fonctionneras que si la fonction est strictement croissante ou decroissante
    x = (x1 + x2) / 2
    while fabs(x1) + fabs(x2) > 1:
        x = (x1 + x2) / 2
        if val(function, x) * val(function, x1) < 0:
            x2 = (x1 + x2) / 2
        elif val(function, x) * val(function, x2) < 0:
            x1 = (x1 + x2) / 2
        elif val(function, x) == 0:
            return x
        else:
            return 'Either this function has no roots, or there is a problem. Please notify the pumpkin master at once.'

    return x


def derivee(function):
    ## ceci est juste pour remplir l'espace blanc
    ok=ok
    ## voila

    ## ce qui suit ne fonctionnera pas! c'est juste une ebauche
    function = separate(function)
    for i in range(len(function)):
        

def separate(function):
    num = []
    ope = []
    t = 0
    for i in range(len(function)):
        if function[i] in ('+', '-', '*', '/'):
            num.append(function[t:i])
            ope.append(function[i])
            t = i + 1
    num.append(function[t:])
    print(num, "\n", ope)
    



if __name__ == '__main__':
   main()
