'''
Este programa va pedir el usuario su pin de acceso. 
1) Si el pin es correcto, entonces el programa debe decirle 
autentificacion exitosa, acceso concedido
2) Si el pin es incorrecto, entonces el programa debe decirle
 pin incorrecto y el numero de intentos
que le quedan.
3) Si el usuario supera el numero de intentos permitidos entonces
 el programa le va a decir numero de intentos superados y cuenta 
bloqueada
'''
PIN_CORRECT = "1234"
TRIES_MAX= 3
tries = 0

while tries < TRIES_MAX:
	entrada = input("Ingresa tu pin (4 digitos)")
	if entrada == PIN_CORRECT:
		print("autentificacion exitosa")
		print("Acceso concedido")
		break
	else:
		tries+=1
		remain=TRIES_MAX - tries
		if remain>0:
			print(f"Pin Incorrecto. Te quedan {remain} intentos")
		else:
			print("CUENTA BLOQUEADA")

