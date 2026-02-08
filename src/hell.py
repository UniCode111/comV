name = "Hola bastardos"
print(name)
# Built-in method input(argument)-Se utiliza para que el usuario ingrese informacion 
user_name = input("Cómo te llamas")
edad_txt = input("Cuál es tu edad")

#Built-in method type(1 argument)-Nos dice el tipo de variable del argumento
print(user_name)
print(type(user_name))
print(edad_txt)
print(type(edad_txt))

#Method built-in int(1-argument)-Convierte un str a int
try:
	edad=int(edad_txt)
	print(type(edad))
	print(edad)
except ValueError:
	print("Error: La conversion no se pudo realizar")
	print("Debes ingresar un numero entero")
print("FIN")
