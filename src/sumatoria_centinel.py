
print("Este programa captura importes")
info = """
**************************************************************************

	Este programa lleva el conteo de cuantos importes ha
	introducido un usuario.
	
	Va acumulando todos los importes que el usuario ingresa.
	Si el usuario desea terminar el programa puede escribir
	en cualquier momento la palabra exit, quit, terminar, etc.

			Elaborado por yo

//////////////////////////////////////////////////////////////////////////
**************************************************************************
"""

print(info)
conteo=0
suma=0.0
minimo = None
maximo = None

while True:
	user_message="""
	Ingresa tu importe (MXN)
	Si quieres dejar de capturar importes
	puedes ingresar en cualquier momento
	exit, quit, terminar. 
"""
	line = input(user_message).lower()
	if line == "exit" or line == "quit" or line == "terminar" or line == "ya porfavor":
		break
	try:
		value = float(line)
	except ValueError:
		print("Valor invalido ")
		continue
	conteo += 1
	suma += value
	
	if minimo is None or value<minimo:
		minimo=value
	if maximo is None or value>maximo:
		maximo = value
if conteo == 0:
	print("No se caputaron importes")
else:
	print("="*80)
	print(f"{conteo}")
	print(f"{suma}")
	print(f"{minimo}")
	print(f"{maximo}")
print("Adios")
