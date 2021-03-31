class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque


''' Primeira Tarefa - Decodificação da Lista de Missões '''


def adicionar_alfabeto(deque, alfabeto):
    [deque.add_front(char) for char in alfabeto]


def decifrar(deque, texto_cifrado, chave):
    ref = deque.__str__()
    temp = [ref[ref.index(char) - chave] for char in texto_cifrado]
    return ''.join(temp)


''' Segunda Tarefa - Selecionar Subconjunto de Missões '''


def selecionar_subconjunto_missoes():
    time, show_missions, order, alphabet, cipher_key, mission_count = int(input()), int(input()), int(input()), input(), int(input()), int(input())
    missions = [''.join([i for i in input() if i != '[' and i != ']']) for i in range(mission_count)]
    return missions


if __name__ == '__main__':
    print(selecionar_subconjunto_missoes())
