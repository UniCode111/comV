peso_txt = input("Peso (kg):")
altura_txt = input("Altura (m):")

try:
	weigth = float(peso_txt)
	heigth = float(altura_txt)
	imc = weigth / heigth**2
except ValueError:
	print("Datos invalidos. Ej.: peso 70.5, altura 1.75")
except ZeroDivisionError:
	print("No se puede dividir sobre 0")
print(f"TU IMC ES {imc}")


