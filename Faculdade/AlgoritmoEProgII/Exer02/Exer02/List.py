from NodeClass import Node


class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, value):
        if self.first:
            aux = self.first
            ant = None
            while (aux.next):
                ant = aux
                aux = aux.next
            aux.next = Node(value)
            aux.next.ant = aux
            aux.ant = ant
            if self.last:
                self.last = aux.next
        else:
            self.first = Node(value)
            self.last = Node(value)
        self.size += 1

    def imprimeEmOrdem(self):
        if self.first == None:
            print("Lista Vazia")

        aux = self.first
        while (aux):
            print(aux.report, end=', ')
            aux = aux.next
        print("\nQtde Nros Lista: "+ str(self.size))
        print(" -----------------\n")

    def imprimeOrdemInversa(self):
        aux = self.last
        print("Lista em Ordem Inversa: ")
        while (aux):
            print(aux.report, end=', ')
            aux = aux.ant
        print("\nQtde Nros Lista: "+ str(self.size))
