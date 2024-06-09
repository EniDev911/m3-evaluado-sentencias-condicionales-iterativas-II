from string import ascii_lowercase
import getpass

intentos = 0
password = getpass.getpass("Ingrese la contraseña a forzar: ")

for i in password:
	for j in ascii_lowercase:
		intentos += 1
		if j == i:
			break

print("La contraseña fue forzada en", intentos, "intentos")