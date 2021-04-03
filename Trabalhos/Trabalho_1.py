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
    ref, current = deque.__str__(), ''
    temp = [ref[ref.index(char) - chave] for char in texto_cifrado]
    while current != temp[-1]:
        current = deque.remove_rear()
        deque.add_front(current)
    deque.add_rear(deque.remove_front())
    return ''.join(temp)


''' Segunda Tarefa - Selecionar Subconjunto de Missões '''


def selecionar_subconjunto_missoes():
    time, show_missions, order, alphabet, cipher_key, mission_count = int(input()), int(input()), int(input()), input(), int(input()), int(input())
    encrypted_missions = [''.join([i for i in input() if i != '[' and i != ']']) for i in range(mission_count)]
    d = Deque()
    adicionar_alfabeto(d, alphabet)
    all_missions = [decifrar(d, encrypted, cipher_key).split(',') for encrypted in encrypted_missions]
    all_missions = [[mission[0], int(mission[1]), int(mission[2]), mission[3]] for mission in all_missions]
    times, values = [mission[1] for mission in all_missions], [mission[2] for mission in all_missions]
    matrix = [[0 if j == 0 or i == 0 else -1 for j in range(time + 1)] for i in range(mission_count + 1)]

    def backpack(index, values, times, time_available):
        if matrix[index][time_available] == -1:
            if times[index - 1] > time_available:
                matrix[index][time_available] = backpack(index - 1, values, times, time_available)
            else:
                used = values[index - 1] + backpack(index - 1, values, times, time_available - times[index - 1])
                not_used = backpack(index - 1, values, times, time_available)
                matrix[index][time_available] = used if used > not_used else not_used
        return matrix[index][time_available]

    backpack(mission_count, values, times, time)
    missions_done = build_solutions(matrix, all_missions)
    printer(missions_done, time, order, show_missions)


def build_solutions(matrix, all_missions):
    index, time, missions_done = len(matrix) - 1, len(matrix[0]) - 1, []
    for i in range(index, 0, -1):
        if matrix[i][time] == matrix[i - 1][time - all_missions[i - 1][1]] + all_missions[i - 1][2]:
            missions_done.append(all_missions[i - 1])
            time -= missions_done[-1][1]
    return missions_done


def printer(missions_done, total_time, order, show):
    time_left, final_value = total_time - sum([mission[1] for mission in missions_done]), sum([mission[2] for mission in missions_done])
    missions_done = [[str(value) for value in mission] for mission in missions_done]
    indexes = [index for index in range(4) if index != order]
    missions_done = sorted(missions_done, key=lambda x: (x[order], x[indexes[0]], x[indexes[1]], x[indexes[2]]))
    if show: [print(', '.join(mission)) for mission in missions_done]
    print(f'Tempo restante: {time_left}')
    print(f'Valor: {final_value}')


if __name__ == '__main__':
    d = Deque()
    adicionar_alfabeto(d, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    print(decifrar(d, "XTYSLKNLCL", 27))
    print(d)
    print(decifrar(d, "XTYSLKNLCL", 27))
    print(d)
