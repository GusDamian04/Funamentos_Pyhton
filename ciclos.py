# Ciclos
# while ex_booleana:

i = 1
num = 24
while i <= 10:
    print(f"{ num } * { i } = { num * i }")
    i += 1
else:
    print("Termina el ciclo")

# Ciclo for
# permite recorrer iterables
# iterable -> onjeto que se puede recorrer
# for item in interable:

my_string = "Hola a Todos"
for letter in my_string:
    print(letter, end=', ')
print()

my_list = ["uno", "dos", "tres", "cuatro"]
for item in my_list:
    print(item, end=', ')
print()

# funcion range()
# range (end)
for i in range(10):
    print(i, end=', ')
print()
# range (start, end)
for i in range(10, 20):
    print(i, end=', ')
print()
# range (start, end, setp)
for i in range(10, 100, 10):
    print(i, end=', ')
print()
