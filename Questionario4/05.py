def rotaciona_esquerda(raiz):
    if raiz is None:
        return None

    if raiz.dir is None:
        return raiz

    new = raiz.dir
    raiz.dir = new.esq
    new.esq = raiz
    return new
