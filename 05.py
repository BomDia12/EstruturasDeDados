def primo(n):
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        else:
            i += -1
    return True


def primos_gemeos(n):
    result = []
    last = 3
    while len(result) < n:
        if primo(last) & primo(last + 2):
            result.append((last, last + 2))
            last += 2
        else:
            last += 2
    return result
