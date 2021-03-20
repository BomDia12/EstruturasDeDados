class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()

        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


def removerSegundaOcorrencia(L, n):
    found, done = False, False
    current = L.head
    temp = []
    for i in range(L.size()):
        if current.getData() == n and found and not done:
            done = True
        elif current.getData() == n and not done and not found:
            found = True
            temp.append(current.getData())
        else:
            temp.append(current.getData())
        current = current.getNext()
    res = UnorderedList()
    temp.reverse()
    for i in temp:
        res.add(i)
    return res


if __name__ == '__main__':
    L = UnorderedList()
    L.add(42)
    L.add(42)
    L.add(42)
    L = removerSegundaOcorrencia(L, 42)
    L = removerSegundaOcorrencia(L, 42)
    print(f'Lista: {L}')
