#Colecciones
#Listas
# [item1, itrm2, item_n]
my_list=[1,"Dos",3.14,True, "Otro"]
print(type(my_list))

my_list.append("New item")
my_list.remove(1)
print(my_list.pop())
print(my_list.reverse())

#Indexing
print(my_list[3])
my_list[0]="Camnia de Valor"
print(my_list)

other_list=[3, 1, 4, 8, 2, 6, 4]
other_list.reverse()
print(other_list)
other_list.sort()
print(other_list)

#Slicing
print(other_list[:3])
print(other_list[3:])