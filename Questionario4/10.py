def verificaSimetria(raiz):
    def recursive(left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.dado != right.dado:
            return False

        return recursive(left.esq, right.dir) and recursive(left.dir, right.esq)

    return recursive(raiz.esq, raiz.dir)
