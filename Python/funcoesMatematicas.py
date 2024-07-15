import math


def somaRaizes(a, b):
    result = float(math.sqrt(a) + math.sqrt(b))
    return result


def potencia(a, b):
    result = int(a**b)
    return result


def multiplicaPotencias(a, b):
    x = a**b
    y = b**a
    result = int(x*y)
    return result
