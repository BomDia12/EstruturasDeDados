"""Bom dia! Você já chegou aqui, então você já sabe quem eu sou, seu objetivo agora é fazer a função para
desencriptar o texto, a string encriptada é 'rob emdrmx ctm adupoáeio urAi omoa' boa sorte!"""


def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def encode(key, plaintext):
    order = {
      int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''

    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
