
def moeda(p):
    p = int(p)
    p = str(p)
    p = f'R${p},00'
    return p

def metade(p, show=False):
    p = p / 2
    if show:
        p = moeda(p)
    return p

def dobro(p, show=False):
    p = p * 2
    if show:
        p = moeda(p)
    return p

def aumentar(p, a, show=False):
    a = a / 100
    p += p * a
    if show:
        p = moeda(p)
    return p

def diminuir(p, a, show=False):
    a = a / 100
    p -= p * a
    if show:
        p = moeda(p)
    return p
