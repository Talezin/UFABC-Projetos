import math


def calculaDelta(a, b, c):
    delta = b**2-(4*a*c)
    return delta


def calculaSolucao1(a, b, delta):
    solucao1 = ((-b) + math.sqrt(delta))/(2*a)
    return solucao1


def calculaSolucao2(a, b, delta):
    solucao2 = ((-b) - math.sqrt(delta))/(2*a)
    return solucao2
