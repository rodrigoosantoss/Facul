from List import List

list = List()
list.add(7)
list.add(9)
list.add(2)
print("Lista em ordem de inserção: " + str(list.size))
list.printListOrdered()
list.printReverseOrder()

value = input("Enter a value: ")
list.add(value)
print("\n *********************\n")
list.printListOrdered()
list.printReverseOrder()
