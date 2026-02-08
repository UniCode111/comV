names = []
print(names)

#Metodo append para agregar elementos al final de la lista
names.append("Charly")
names.append("Mar")

print(names)
print(type(names))
print(len(names))
#Metodo insert para agregar elementos en una posicion deseada
names.insert(1, "Alexis")
print(names)

#Metodo pop para sin indice eliminar el ultimo elemento de la lista
names.pop()
print(names)

names.append("Becky")
names.insert(0, "Boslinkord")
#Metodo pop con indice para eliminar un elemento deseado dado un indice
names.pop(2)
print(names)

#Metodo remove(val) para eliminar elementos por valor
names.remove("Charly")
print(names)

names.remove("Becky")
print(names)
