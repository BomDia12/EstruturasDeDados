def em_lista(raiz):
    if raiz.dir is None and raiz.esq is None:
        return raiz

    if raiz.dir is None:
        raiz.esq = em_lista(raiz.esq)
        return raiz

    raiz = rotacao_esquerda(raiz)
    if raiz.dir is None:
        raiz.esq = em_lista(raiz.esq)
        return raiz

    raiz.dir = em_lista(raiz.dir)
    raiz.esq = em_lista(raiz.esq)
    return raiz
