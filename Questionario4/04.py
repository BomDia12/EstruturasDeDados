def comprime(raiz, vezes):
    if vezes == 0:
        return raiz
    else:
        raiz = rotaciona_direita(raiz)
        raiz.esq = comprime(raiz.esq, vezes - 1)
        return raiz
