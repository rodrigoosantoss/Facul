from List import List

list = List()
list.add(4)
list.add(12)
list.add(15)
print("Lista em Ordem: ")
list.imprimeEmOrdem()
list.imprimeOrdemInversa()

print("\n--------------------------")
value = input("Digite um valor: ")

list.add(value)

list.imprimeEmOrdem()
list.imprimeOrdemInversa()