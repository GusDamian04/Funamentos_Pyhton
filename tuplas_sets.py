#Más colecciones en Python

#Tuplas
#(item1, item2, item3)
# Listas son mutables
#tublas inmutables
my_tuple = (1, "Dos", 3.1, True)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
#Error
#my_tuple[0] = 'Algo mas'

# Conjuntos Sets
# desordenados
# mutable
# no permite dublicados
my_set = {"uno", "dos", "tres", "uno"}
print(type(my_set))
print(my_set)
my_set.add(4)
print(my_set)

a = {1, 2, 3, 4 }
b = {3, 4, 5, 6 }
print(a.union(b))
print(a.intersection(b))